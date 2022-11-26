from rest_framework import serializers

from shop import models
from core.serializer import CoreSerializer


class BaseItemSerializer(CoreSerializer):
    type = serializers.ReadOnlyField()
    # image = serializers.Pref

    class Meta(CoreSerializer.Meta):
        model = models.BaseItems
        exclude = CoreSerializer.Meta.exclude + ['en_name']


class AmmoSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Ammo


class ResourceSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Resources


class ShipSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Ships


class EngineSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Engines


class DeviceSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Devices


class WeaponSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Weapons


class DroidSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Droids


class ItemTypeSerializer(CoreSerializer):
    class Meta(CoreSerializer.Meta):
        model = models.ItemsType
