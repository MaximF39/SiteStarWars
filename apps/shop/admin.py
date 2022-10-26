from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class BaseAttributes(admin.ModelAdmin):
    list_display = ('name', 'cost', 'image_img', 'type')

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40"/>')
        else:
            return ''

    image_img.short_description = 'Изображение'


@admin.register(Ammo)
class AmmoAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': ('damage',)
        }),
    )


@admin.register(Resources)
class ResourcesAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': ('effects',)
        }),
    )


@admin.register(Ships)
class ShipsAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': (
            'max_energy', 'weapon_slots', 'device_slots', 'armor', 'shields', 'cpu', 'radar', 'speed', 'max_health',
            'effects', 'droid_slots', 'restrictions')
        }),
    )

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40"/>')
        else:
            return ''

    image_img.short_description = 'Изображение'


@admin.register(Engines)
class EnginesAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': ('hyperjump_radius', 'energy_cost', 'max_health')
        }),
    )


@admin.register(Devices)
class DevicesAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': ('reload_time', 'energy_cost', 'effects', 'max_health', 'device_type', 'restrictions')
        }),
    )


@admin.register(Weapons)
class WeaponsAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': (
            'auto_shots', 'radius', 'reload_time', 'energy_cost', 'min_damage', 'max_damage', 'ammo_class', 'need_cpu',
            'effects', 'max_health', 'weapon_type', 'restrictions')
        }),
    )


@admin.register(Droids)
class DroidsAdmin(BaseAttributes):
    fieldsets = (
        (None, {
            'fields': ('name', 'en_name', 'class_number', 'cost', 'size', 'type', 'image')
        }),
        ('Параметры', {
            'fields': ('energy_cost', 'armor', 'droid_type', 'weapon_class', 'max_health', 'restrictions')
        }),
    )

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
