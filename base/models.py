from django.db import models
from django.contrib.auth.models import User


class AbstractBase(models.Model):
    blocked = models.BooleanField(default=False,)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
