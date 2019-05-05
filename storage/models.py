from django.db import models
from polymorphic.models import PolymorphicModel

from base.models import AbstractBase
from warehouse.models import WarehouseCell
from product.models import Product, StorageUnit, ContainerParams


class Container(AbstractBase):
    cont_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            import uuid
            self.barcode = uuid.uuid4().hex[:20].upper()
        super(Container, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.cont_type.name) + " " + str(self.pk)


class ContainerProducts(AbstractBase):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Номенклатура")
    date = models.DateField(null=True, blank=True, verbose_name="Срок годности")
    unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE, verbose_name="Единица хранения")
    amount = models.IntegerField(verbose_name="Количество")


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE, verbose_name="Ячейка")
    container = models.ForeignKey(Container, on_delete=models.CASCADE, null=True, blank=True)
