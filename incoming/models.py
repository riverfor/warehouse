from django.db import models, transaction

from base.models import AbstractBase
from storage.models import Storage, ContainerProducts, Container
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit, ContainerParams
from django.core.exceptions import ValidationError
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


class DocumentEntry(Storage):
    doc_plan = models.ForeignKey(DocumentPlan, on_delete=models.CASCADE, null=True)
    nomenclature = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    container_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE, null=True, blank=True)

    def check_product(self):
        plan = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature)

        plan_amount = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature).\
            aggregate(Sum('plan'))

        fact_amount = DocumentProducts.objects.filter(document=self.doc_plan, product=self.nomenclature).\
            aggregate(Sum('fact'))

        if plan.count() == 0:
            raise ValidationError("Данного товара нет в документе прихода")
        elif plan_amount['plan__sum'] < self.quantity:
            raise ValidationError("Превышение планового количества")
        elif plan_amount['plan__sum'] - fact_amount['fact__sum'] < self.quantity:
            raise ValidationError("Превышение поланового количества")
        else:
            return True

    def update_plan(self):
        product_entry = self.doc_plan.documentproducts_set.get(product=self.nomenclature)
        if self.pk is None:
            product_entry.fact += self.quantity
        else:
            quantity = self.doc_plan.documententry_set.filter(nomenclature=self.nomenclature).\
                exclude(pk=self.pk).aggregate(Sum('quantity'))
            if quantity['quantity__sum'] is None:
                amount = 0
            else:
                amount = quantity['quantity__sum']

            product_entry.fact = amount + self.quantity
        product_entry.save()

    def create_container(self):
        if self.container_type is None:
            self.container_type = self.nomenclature.base_cont_type

        import uuid
        if self.pk is None:
            cont = Container.objects.create(cont_type=self.container_type, barcode=uuid.uuid4().hex[:20].upper())
            if cont:
                return cont
            else:
                raise ValidationError("Ошибка создания контейнера")
        else:
            return self.container

    def add_product_to_container(self, container):
        if self.pk is None:
            ContainerProducts.objects.create(container=container, product=self.nomenclature, unit=self.storage_unit,
                                         amount=self.quantity)
        else:
            container = ContainerProducts.objects.get(pk=self.container.pk)
            container.amount = self.quantity
            container.save()

    @transaction.atomic
    def save(self, *args, **kwargs):
        check_product = self.check_product()
        if check_product:
            container = self.create_container()
            self.add_product_to_container(container)
            self.update_plan()
            self.container = container
            self.cell = self.doc_plan.cell
            super(DocumentEntry, self).save(*args, **kwargs)
