import uuid
from base.models import AbstractBase, models

STORAGE = 1
ACCEPTANCE = 2
SHIPMENT = 3

CELL_TYPE_CHOICES = (
    (STORAGE, 'Storage'),
    (ACCEPTANCE, 'Acceptance'),
    (SHIPMENT, 'Shipment'),
)


class Rack (AbstractBase):
    name = models.CharField(max_length=2, verbose_name="Название", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стеллаж"
        verbose_name_plural = "Стеллажи"


class Tier (AbstractBase):
    name = models.CharField(max_length=2, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class Position (AbstractBase):
    name = models.CharField(max_length=2, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class WarehouseCell (AbstractBase):
    name = models.CharField(max_length=20, null=True, blank=True)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, verbose_name="Стеллаж", null=True, blank=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, verbose_name="Ярус", null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Позиция", null=True, blank=True)
    cell_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    cell_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    cell_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')
    barcode = models.CharField(max_length=20, null=True, blank=True, unique=True, verbose_name="Штрих код")
    cell_type = models.PositiveSmallIntegerField(choices=CELL_TYPE_CHOICES, default=STORAGE, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.barcode = uuid.uuid4().hex[:20].upper()
            if self.name is None:
                self.name = str(self.rack.name) + "-" + str(self.tier.name) + "-" + str(self.position.name)
        super(WarehouseCell, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"
        unique_together = ('rack', 'tier', 'position', 'name')
