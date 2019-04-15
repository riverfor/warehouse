from django.db import models
from polymorphic.models import PolymorphicModel
from warehouse.models import WarehouseCell


class Storage(PolymorphicModel):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE)
    amount = models.IntegerField()


class DocumentPlanIn(models.Model):
    cell = models.ForeignKey(WarehouseCell, on_delete=models.CASCADE)
    total_plan = models.IntegerField()
    fact = models.IntegerField()


class DocumentIn(Storage):
    doc_plan = models.ForeignKey(DocumentPlanIn, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.amount = self.quantity
        self.cell = self.doc_plan.cell
        super(DocumentIn, self).save(*args, **kwargs)





