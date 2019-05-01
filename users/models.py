from django.contrib.auth.models import AbstractUser
from django.db import models


class Warehouse (models.Model):
    name = models.CharField(max_length=50, default="", verbose_name="Название")
    blocked = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, verbose_name='Основной склад')

    class Meta:
        verbose_name = 'User'
