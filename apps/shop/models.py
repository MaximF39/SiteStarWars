from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel
from django.contrib.postgres.fields import ArrayField


class BaseItems(BaseModel):
    name = models.CharField(max_length=100, null=False, verbose_name="Название")
    en_name = models.CharField(max_length=100, null=False, verbose_name="En название")
    class_number = models.IntegerField(null=False, verbose_name="Номер класса")
    cost = models.IntegerField(null=False, verbose_name="Цена")
    size = models.FloatField(null=False, verbose_name="Размер")
    image = VersatileImageField(null=False, blank=True, upload_to='images', verbose_name="Изображение")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name


class Ammo(BaseItems):
    damage = models.IntegerField(null=False, verbose_name="Урон")
    type = models.CharField(max_length=20, auto_created="ammo")

    class Meta:
        verbose_name = "Боекомплект"
        verbose_name_plural = "Боекомплект"

class Resources(BaseItems):
    effects = ArrayField(ArrayField(models.IntegerField()))
    type = models.CharField(max_length=20, auto_created="resource")

    class Meta:
        verbose_name = "Ресурс"
        verbose_name_plural = "Ресурсы"


class Ships(BaseItems):
    max_energy = models.IntegerField(null=False)
    weapon_slots = models.IntegerField(null=False)
    device_slots = models.IntegerField(null=False)
    armor = models.IntegerField(null=False)
    shields = models.IntegerField(null=False)
    cpu = models.IntegerField(null=False)
    radar = models.IntegerField(null=False)
    speed = models.IntegerField(null=False)
    max_health = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.IntegerField(null=False)))
    droid_slots = models.IntegerField(null=False)
    restrictions = models.JSONField()
    type = models.CharField(max_length=20, auto_created="ship")


    class Meta:
        verbose_name = "Корабль"
        verbose_name_plural = "Корабли"


class Engines(BaseItems):
    hyperjump_radius = models.IntegerField(null=False)
    energy_cost = models.IntegerField(null=False)
    max_health = models.IntegerField(null=False)
    type = models.CharField(max_length=20, auto_created="engine")

    class Meta:
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"


class Devices(BaseItems):
    reload_time = models.IntegerField(null=False)
    energy_cost = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.IntegerField(null=False)))
    max_health = models.IntegerField(null=False)
    device_type = models.IntegerField(null=False)
    restrictions = models.JSONField()
    type = models.CharField(max_length=20, auto_created="device")

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class Weapons(BaseItems):
    auto_shots = models.IntegerField(null=False)
    radius = models.IntegerField(null=False)
    reload_time = models.IntegerField(null=False)
    energy_cost = models.IntegerField(null=False)
    min_damage = models.IntegerField(null=False)
    max_damage = models.IntegerField(null=False)
    ammo_class = models.ForeignKey('Ammo', on_delete=models.SET_NULL, null=True)
    need_cpu = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.IntegerField(null=False)))
    max_health = models.IntegerField(null=False)
    weapon_type = models.IntegerField(null=False)
    restrictions = models.JSONField()
    type = models.CharField(max_length=20, auto_created="weapon")

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"


class Droids(BaseItems):
    energy_cost = models.IntegerField(null=False)
    armor = models.IntegerField(null=False)
    droid_type = models.IntegerField(null=False)
    weapon_class = models.ForeignKey('Weapons', on_delete=models.SET_NULL, null=True)
    max_health = models.IntegerField(null=False)
    restrictions = models.JSONField()
    type = models.CharField(max_length=20, auto_created="droid")

    class Meta:
        verbose_name = "Дройд"
        verbose_name_plural = "Дройды"
