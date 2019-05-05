from django.db import models, transaction
from rest_framework import serializers
from base.models import AbstractBase
from storage.models import Storage, ContainerProducts, Container
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit, ContainerParams
from django.db.models import Sum


class DocumentPlan(AbstractBase):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name='Адрес приемки')
    bill = models.CharField(max_length=50, null=True, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)


class DocumentProducts(AbstractBase):
    document = models.ForeignKey(DocumentPlan, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE, verbose_name='Единица хранения')
    plan = models.IntegerField(verbose_name='Плановое количество базовых едениц')
    fact = models.IntegerField(verbose_name='Фактическое количество базовых едениц', default=0)

    class Meta:
        unique_together =(
            'document',
            'product',
        )


class DocumentEntry(Storage):
    doc_plan = models.ForeignKey(DocumentPlan, on_delete=models.CASCADE, null=True)
    nomenclature = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    container_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE, null=True, blank=True)
    in_container = models.ForeignKey('storage.Container', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    def check_unit(self):
        if self.storage_unit.product != self.nomenclature:
            raise serializers.ValidationError("Указана некорретная единица хранения")

    def check_product(self):
        plan = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature)

        plan_amount = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature).\
            aggregate(Sum('plan'))

        fact_amount = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature).\
            aggregate(Sum('fact'))

        if plan.count() == 0:
            raise serializers.ValidationError("Данного товара нет в документе прихода")
        elif plan_amount['plan__sum'] < self.quantity:
            raise serializers.ValidationError("Превышение планового количества")
        elif plan_amount['plan__sum'] - fact_amount['fact__sum'] < self.quantity:
            raise serializers.ValidationError("Превышение поланового количества")
        else:
            return True

    def update_plan(self):
        product_entry = self.doc_plan.products.get(product=self.nomenclature)
        if self.pk is None:
            product_entry.fact += self.quantity
        else:
            quantity = self.doc_plan.products.filter(nomenclature=self.nomenclature).\
                exclude(pk=self.pk).aggregate(Sum('quantity'))
            if quantity['quantity__sum'] is None:
                amount = 0
            else:
                amount = quantity['quantity__sum']

            product_entry.fact = amount + self.quantity
        product_entry.save()

    def create_container(self):
        if self.in_container is None:
            if self.container_type is None:
                self.container_type = self.nomenclature.base_cont_type

            if self.pk is None:
                cont = Container.objects.create(cont_type=self.container_type, owner=self.owner)
                if cont:
                    return cont
                else:
                    raise serializers.ValidationError("Ошибка создания контейнера")
            else:
                return self.container
        else:
            return self.in_container

    def add_product_to_container(self, container):
        if self.pk is None:
            ContainerProducts.objects.create(container=container, product=self.nomenclature, unit=self.storage_unit,
                                         amount=self.quantity, owner=self.owner)
        else:
            container = ContainerProducts.objects.get(pk=self.container.pk)
            container.amount = self.quantity
            container.save()

    def check_container_stock(self, container):
        if self.nomenclature.model.use_mono_container is True:
            stock = ContainerProducts.objects.filter(container=container)

            if stock.count() == 0:
                return True
            else:
                mass = []
                mass.append(self.nomenclature)
                if stock.filter(product__in=mass).count() == 1:
                    return True
                else:
                    raise serializers.ValidationError('В данном контейнере уже находится другой продукт')
        else:
            return True

    @transaction.atomic
    def save(self, *args, **kwargs):
        check_product = self.check_product()
        self.check_unit()
        if check_product:
            container = self.create_container()
            self.check_container_stock(container)
            self.add_product_to_container(container)
            self.update_plan()
            self.container = container
            self.cell = self.doc_plan.cell
            super(DocumentEntry, self).save(*args, **kwargs)
