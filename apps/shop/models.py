from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel
from django.contrib.postgres.fields import ArrayField


class BaseItems(BaseModel):
    name = models.CharField(max_length=100, null=False)
    classNumber = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
    size = models.FloatField(null=False)
    image = VersatileImageField(null=False, blank=True, upload_to='images')

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class Ammo(BaseItems):
    damage = models.SmallIntegerField(null=False)


class Resources(BaseItems):
    effects = ArrayField(ArrayField(models.SmallIntegerField(null=False)))


class Ships(BaseItems):
    maxEnergy = models.IntegerField(null=False)
    weaponSlots = models.SmallIntegerField(null=False)
    deviceSlots = models.SmallIntegerField(null=False)
    armor = models.IntegerField(null=False)
    shields = models.SmallIntegerField(null=False)
    cpu = models.SmallIntegerField(null=False)
    radar = models.SmallIntegerField(null=False)
    restrictions = models.JSONField(null=False)
    speed = models.SmallIntegerField(null=False)
    maxHealth = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.SmallIntegerField(null=False)))
    droidSlots = models.SmallIntegerField(null=False)


class Engines(BaseItems):
    hyperjumpRadius = models.SmallIntegerField(null=False)
    energyCost = models.SmallIntegerField(null=False)
    maxHealth = models.IntegerField(null=False)


class Devices(BaseItems):
    reloadTime = models.SmallIntegerField(null=False)  # ms
    energyCost = models.SmallIntegerField(null=False)
    effects = ArrayField(ArrayField(models.SmallIntegerField(null=False)))
    restrictions = models.JSONField(null=False)
    maxHealth = models.IntegerField(null=False)
    device_type = models.SmallIntegerField(null=False)


class Weapons(BaseItems):
    autoShots = models.SmallIntegerField(null=False)
    radius = models.SmallIntegerField(null=False)
    reloadTime = models.SmallIntegerField(null=False)
    energyCost = models.SmallIntegerField(null=False)
    minDamage = models.SmallIntegerField(null=False)
    maxDamage = models.SmallIntegerField(null=False)
    restrictions = models.JSONField(null=False),
    ammoClass = models.OneToOneField(
        Ammo,
        on_delete=models.CASCADE,
    )
    needCpu = models.SmallIntegerField(null=False)
    effects = ArrayField(ArrayField(models.SmallIntegerField(null=False)))
    maxHealth = models.IntegerField(null=False)
    weaponType = models.SmallIntegerField(null=False)
class Droids(BaseItems):
    energyCost = models.SmallIntegerField(null=False)
    armor = models.SmallIntegerField(null=False)
    droidType = models.SmallIntegerField(null=False)
    weaponClass = models.OneToOneField(
        Weapons,
        on_delete=models.CASCADE,
    )
    restrictions = models.JSONField(null=False)
    maxHealth = models.IntegerField(null=False)
