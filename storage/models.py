from django.db import models
from polymorphic.models import PolymorphicModel
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE)
    amount = models.IntegerField()


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
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.amount = self.quantity
        self.cell = self.doc_plan.cell
        super(DocumentIn, self).save(*args, **kwargs)





