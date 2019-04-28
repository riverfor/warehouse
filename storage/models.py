from django.db import models
from polymorphic.models import PolymorphicModel
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit, ContainerParams


class Container(models.Model):
    cont_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=20, unique=True)


class ContainerProducts(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Номенклатура")
    date = models.DateField(null=True, blank=True, verbose_name="Срок годности")
    unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE, verbose_name="Единица хранения")
    amount = models.IntegerField(verbose_name="Количество")


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name="Ячейка")
    container = models.ForeignKey(Container, on_delete=models.CASCADE, null=True, blank=True)





