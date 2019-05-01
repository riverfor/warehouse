import uuid
from base.models import AbstractBase, models
from django.contrib.auth.models import User


class Warehouse (AbstractBase):
    name = models.CharField(max_length=50, default="", verbose_name="Название")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Rack (AbstractBase):
    name = models.CharField(max_length=2, verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стеллаж"
        verbose_name_plural = "Стеллажи"


class WarehouseCell (AbstractBase):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, verbose_name="Стеллаж")
    tier = models.CharField(max_length=2, verbose_name="Ярус")
    position = models.CharField(max_length=2, verbose_name="Позиция")
    cell_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    cell_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    cell_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')
    barcode = models.CharField(max_length=20, null=True, blank=True, unique=True, verbose_name="Штрих код")

    def __str__(self):
        return str(self.rack.name) + "-" + str(self.tier) + "-" + str(self.position)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.barcode = uuid.uuid4().hex[:20].upper()
        super(WarehouseCell, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"
        unique_together = ('rack', 'tier', 'position')

