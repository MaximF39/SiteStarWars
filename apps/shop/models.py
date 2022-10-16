from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel

# Create your models here.
class BaseItem(BaseModel):
    name = models.CharField(max_length=100, null=False)
    classNumber = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
    size = models.FloatField(null=False)
    image = VersatileImageField(null=False, blank=True, upload_to='images')

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

# class AmmoItem(BaseItem):
#     damage = models.SmallIntegerField(null=False)
