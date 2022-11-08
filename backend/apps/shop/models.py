from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import CoreModel
from django.contrib.postgres.fields import ArrayField


class BaseItems(CoreModel):
    name = models.CharField(max_length=100, null=False, verbose_name="Название")
    class_number = models.IntegerField(verbose_name="Номер класса")
    en_name = models.CharField(max_length=100, null=False, verbose_name="En название")
    cost = models.IntegerField(null=False, verbose_name="Цена")
    size = models.FloatField(null=False, verbose_name="Размер")
    image = models.ImageField(max_length=255, null=False, blank=True, verbose_name="Изображение")
    @property
    def type(self):
        return self.__class__.__name__

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class Ammo(BaseItems):
    damage = models.IntegerField(null=False, verbose_name="Урон")

    class Meta:
        verbose_name = "Патрон"
        verbose_name_plural = "Патроны"

class Resources(BaseItems):
    effects = ArrayField(ArrayField(models.IntegerField()), null=True)

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
    effects = ArrayField(ArrayField(models.IntegerField()), null=True)
    droid_slots = models.IntegerField(null=False)
    restrictions = models.JSONField(null=True)
    max_health = models.IntegerField(null=False)


    class Meta:
        verbose_name = "Корабль"
        verbose_name_plural = "Корабли"


class Engines(BaseItems):
    hyperjump_radius = models.IntegerField(null=False)
    energy_cost = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"


class Devices(BaseItems):
    reload_time = models.IntegerField(null=False)
    energy_cost = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.IntegerField()), null=True)
    device_type = models.IntegerField(null=False)
    restrictions = models.JSONField(null=True)

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
    weapon_ammo = models.ForeignKey('Ammo', on_delete=models.CASCADE, null=True)
    need_cpu = models.IntegerField(null=False)
    effects = ArrayField(ArrayField(models.IntegerField()), null=True)
    weapon_type = models.IntegerField(null=False)
    restrictions = models.JSONField(null=True)

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"


class Droids(BaseItems):
    energy_cost = models.IntegerField(null=False)
    armor = models.IntegerField(null=False)
    droid_type = models.IntegerField(null=False)
    droid_weapon = models.ForeignKey('Weapons', on_delete=models.CASCADE, null=True)
    restrictions = models.JSONField(null=True)
    max_health = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Дройд"
        verbose_name_plural = "Дройды"

class ItemsType(CoreModel):
    type_en = models.CharField(max_length=50)
    type_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.type_ru

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
