from base.models import AbstractBase, models
from django.contrib.auth.models import User


class Warehouse (AbstractBase):
    name = models.CharField(max_length=50, default="", verbose_name="Название")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "ЯСклады"


class Rack (AbstractBase):
    name = models.CharField(max_length=2, verbose_name="Имя")

    class Meta:
        verbose_name = "Стеллаж"
        verbose_name_plural = "Стеллажи"

    def __str__(self):
        return self.name


class WarehouseCell (AbstractBase):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, verbose_name="Стеллаж")
    tier = models.CharField(max_length=2, verbose_name="Ярус")
    position = models.CharField(max_length=2, verbose_name="Позиция")
    cell_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    cell_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    cell_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"

    def __str__(self):
        return self.rack.name + "-" + self.tier + "-" + self.position
