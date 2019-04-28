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

    def __str__(self):
        return self.container.cont_type.name + " " + self.container.pk + " " + self.product.name


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name="Ячейка")
    container = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __str__(self):
        return self.cell + " " + self.container.cont_type.name + " " + self.container.pk



