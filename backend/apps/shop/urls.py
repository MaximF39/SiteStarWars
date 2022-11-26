from django.urls import path, include

from config.urls import router
from .views import *
from shop import views

router.register(r'base_items', views.BaseItemsViewSet)
router.register(r'ammo', views.AmmoViewSet)
router.register(r'ships', views.ShipViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'engines', views.EngineViewSet)
router.register(r'resources', views.ResourceViewSet)
router.register(r'droids', views.DroidViewSet)
router.register(r'weapons', views.WeaponViewSet)
router.register(r'items_type', views.ItemTypeViewSet)

urlpatterns = [
    path('1', redirect_shop),
    path('', Shop.as_view(), name='shop'),
    path('<slug:item_slug>', ShopFilter.as_view(), name='shop_filter'),
]

