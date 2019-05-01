from django.db import models


class AbstractBase(models.Model):
    blocked = models.BooleanField(default=False,)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    from users.models import User
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
