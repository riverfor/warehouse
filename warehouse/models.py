from base.models import AbstractBase, models
from django.contrib.auth.models import User


class Warehouse (AbstractBase):
    name = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Rack (AbstractBase):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class WarehouseCell (AbstractBase):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    tier = models.CharField(max_length=2)
    position = models.CharField(max_length=2)
    cell_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10)
    cell_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10)
    cell_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10)

    def __str__(self):
        return self.rack.name + "-" + self.tier + "-" + self.position
