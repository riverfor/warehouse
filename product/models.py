from django.db import models


class ContainerParams(models.Model):
    name = models.CharField(max_length=20)
    cont_width = models.IntegerField(verbose_name='Ширина')
    cont_height = models.IntegerField(verbose_name='Высота')
    cont_length = models.IntegerField(verbose_name='Глубина')


class AccountingModelProducts(models.Model):
    name = models.CharField(max_length=50)
    use_date = models.BooleanField(default=False, verbose_name='Учет по срока годности')
    use_serial = models.BooleanField(default=False, verbose_name='Учет по серийным номерам')
    use_parts = models.BooleanField(default=False, verbose_name='Учет по партиям')

    class Meta:
        verbose_name = 'Модель учета'
        verbose_name_plural = 'Модели учета'


class Product(models.Model):
    vendor = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    model = models.ForeignKey(AccountingModelProducts, on_delete=models.CASCADE, verbose_name='Модель учета')
    description = models.TextField(verbose_name='Краткое описание')
    base_cont_type = models.ForeignKey(ContainerParams, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = "Номенклатуры"


class StorageUnitsClass(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Класс единица хранения'
        verbose_name_plural = "Классы единиц хранения"


class StorageUnit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Номенклатура')
    ratio = models.IntegerField(default=1, verbose_name='коэфициент')
    unit_class = models.ForeignKey(StorageUnitsClass, on_delete=models.CASCADE,  verbose_name='Класс единицы хранения')
    unit_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    unit_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    unit_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')

    class Meta:
        verbose_name = 'Единица хранения'
        verbose_name_plural = "Единицы хранения"

