from django.db import models
from polymorphic.models import PolymorphicModel
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit
from django.core.exceptions import ValidationError
from django.db.models import Sum


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name="Ячейка")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Номенклатура")
    unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE, verbose_name="Единица хранения")
    amount = models.IntegerField(verbose_name="Количество")


class DocumentPlanIn(models.Model):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name='Адрес приемки')


class DocumentPlanInProducts(models.Model):
    document = models.ForeignKey(DocumentPlanIn, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE, verbose_name='Единица хранения')
    plan = models.IntegerField(verbose_name='Плановое количество базовых едениц')
    fact = models.IntegerField(verbose_name='Фактическое количество базовых едениц')


class DocumentIn(Storage):
    doc_plan = models.ForeignKey(DocumentPlanIn, on_delete=models.CASCADE, null=True)
    nomenclature = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=50)

    def check_product(self):
        plan = DocumentPlanInProducts.objects.filter(document=self.doc_plan, product=self.nomenclature)
        plan_amount = DocumentPlanInProducts.objects.filter(document=self.doc_plan,
                                                            product=self.nomenclature).aggregate(Sum('plan'))
        fact_amount = DocumentPlanInProducts.objects.filter(document=self.doc_plan,
                                                            product=self.nomenclature).aggregate(Sum('fact'))

        if plan.count() == 0:
            raise ValidationError("Данного товара нет в документе прихода")
        elif plan_amount['plan__sum'] < self.quantity:
            raise ValidationError("Превышение планового количества")
        elif plan_amount['plan__sum'] - fact_amount['fact__sum'] < self.quantity:
            raise ValidationError("Превышение поланового количества")
        else:
            return True

    def save(self, *args, **kwargs):
        check_product = self.check_product()
        if check_product:
            self.amount = self.quantity
            self.cell = self.doc_plan.cell
            super(DocumentIn, self).save(*args, **kwargs)
