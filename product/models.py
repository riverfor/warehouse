from django.db import models

from base.models import AbstractBase


class ContainerParams(AbstractBase):
    name = models.CharField(max_length=20)
    cont_width = models.IntegerField(verbose_name='Ширина')
    cont_height = models.IntegerField(verbose_name='Высота')
    cont_length = models.IntegerField(verbose_name='Глубина')

    def __str__(self):
        return self.name


class AccountingModelProducts(AbstractBase):
    name = models.CharField(max_length=50, verbose_name='Название')
    use_date = models.BooleanField(default=False, verbose_name='Учет по срока годности')
    use_serial = models.BooleanField(default=False, verbose_name='Учет по серийным номерам')
    use_parts = models.BooleanField(default=False, verbose_name='Учет по партиям')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель учета'
        verbose_name_plural = 'Модели учета'


class Product(AbstractBase):
    vendor = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    model = models.ForeignKey(AccountingModelProducts, on_delete=models.CASCADE, verbose_name='Модель учета')
    description = models.TextField(verbose_name='Краткое описание')
    base_cont_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE, verbose_name='Базовый тип паллеты')
    base_unit = models.OneToOneField('product.StorageUnit', on_delete=models.CASCADE, related_name='base_unit',
                                     null=True, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', null=True,
                                blank=True)

    def __str__(self):
        return str(self.vendor) + " " + str(self.name)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = "Номенклатуры"
        unique_together = (
            'vendor',
            'name',
        )


class StorageUnitsClass(AbstractBase):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс единица хранения'
        verbose_name_plural = "Классы единиц хранения"


class StorageUnit(AbstractBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='units', verbose_name='Номенклатура')
    ratio = models.IntegerField(default=1, verbose_name='коэфициент')
    unit_class = models.ForeignKey(StorageUnitsClass, on_delete=models.CASCADE,  verbose_name='Класс единицы хранения')
    unit_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    unit_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    unit_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')

    def __str__(self):
        return str(self.product.name) + ' | ' + str(self.unit_class.name) + str(" (") + str(self.ratio) + str(")")

    class Meta:
        verbose_name = 'Единица хранения'
        verbose_name_plural = "Единицы хранения"
        unique_together = ('product', 'ratio',)

