from django.db import models


class AccountingModelProducts(models.Model):
    name = models.CharField(max_length=50)
    use_date = models.BooleanField(default=False, verbose_name='Учет по срока годности')
    use_serial = models.BooleanField(default=False, verbose_name='Учет по серийным номерам')
    use_parts = models.BooleanField(default=False, verbose_name='Учет по партиям')

    class Meta:
        verbose_name = 'Модель учета'
        verbose_name_plural = 'Модели учета'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    model = models.ForeignKey(AccountingModelProducts, on_delete=models.CASCADE, verbose_name='Модель учета')
    description = models.TextField(verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = "Номенклатуры"

    def __str__(self):
        return self.name


class StorageUnitsClass(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Класс единица хранения'
        verbose_name_plural = "Классы единиц хранения"

    def __str__(self):
        return self.name


class StorageUnit(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, verbose_name='Номенклатура')
    ratio = models.IntegerField(default=1, verbose_name='коэфициент')
    unit_class = models.ForeignKey(StorageUnitsClass, on_delete=models.CASCADE,  verbose_name='Класс единицы хранения')
    unit_width = models.DecimalField(max_digits=5, decimal_places=3,  max_length=10, verbose_name='Ширина')
    unit_height = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Высота')
    unit_length = models.DecimalField(max_digits=5, decimal_places=3, max_length=10, verbose_name='Глубина')

    class Meta:
        verbose_name = 'Единица хранения'
        verbose_name_plural = "Единицы хранения"

    def __str__(self):
        return self.product.name + " " + self.unit_class.name
