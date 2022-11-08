import json

from django.shortcuts import redirect
from django.views.generic import ListView
from rest_framework import viewsets, permissions

from shop import models, serializer

class BaseItemsViewSet(viewsets.ModelViewSet):
    queryset = models.BaseItems.objects.all()
    serializer_class = serializer.BaseItemSerializer
    permission_classes = [permissions.AllowAny]

class AmmoViewSet(viewsets.ModelViewSet):
    queryset = models.Ammo.objects.all()
    serializer_class = serializer.AmmoSerializer
    permission_classes = [permissions.AllowAny]

class ShipViewSet(viewsets.ModelViewSet):
    queryset = models.Ships.objects.all()
    serializer_class = serializer.ShipSerializer
    permission_classes = [permissions.AllowAny]
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = models.Devices.objects.all()
    serializer_class = serializer.DeviceSerializer
    permission_classes = [permissions.AllowAny]
class EngineViewSet(viewsets.ModelViewSet):
    queryset = models.Engines.objects.all()
    serializer_class = serializer.EngineSerializer
    permission_classes = [permissions.AllowAny]
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resources.objects.all()
    serializer_class = serializer.ResourceSerializer
    permission_classes = [permissions.AllowAny]
class DroidViewSet(viewsets.ModelViewSet):
    queryset = models.Droids.objects.all()
    serializer_class = serializer.DroidSerializer
    permission_classes = [permissions.AllowAny]
class WeaponViewSet(viewsets.ModelViewSet):
    queryset = models.Weapons.objects.all()
    serializer_class = serializer.WeaponSerializer
    permission_classes = [permissions.AllowAny]
class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ItemsType.objects.all()
    serializer_class = serializer.ItemTypeSerializer
    permission_classes = [permissions.AllowAny]

class Shop(ListView):
    paginate_by = 10
    template_name = 'shop/shop.html'
    context_object_name = 'items'
    object_list = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = models.ItemsType.objects.all()
        select_type = 1
        context['select_type'] = select_type
        context['types'] = types
        return context

    def get_queryset(self):
        model = models.BaseItems.objects.all().order_by('id')
        return model


class ShopFilter(ListView):
    paginate_by = 10
    template_name = 'shop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = models.ItemsType.objects.all()
        select_type = int(self.kwargs['item_slug'])
        context['select_type'] = select_type
        context['types'] = types
        return context

    def get_queryset(self):
        select_type = int(self.kwargs['item_slug'])
        types = models.ItemsType.objects.all()
        en_name = types[select_type - 1].type_en
        model_items = getattr(models, en_name).objects.all().order_by('id')
        print(AmmoSerializer(models.Ammo.objects.all()[0]).data)

        return model_items


def redirect_shop(request):
    return redirect('shop')
