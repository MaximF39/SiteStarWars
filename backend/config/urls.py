from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from shop import views

router = routers.DefaultRouter()
router.register(r'base_items', views.BaseItemsViewSet)
router.register(r'ammo', views.AmmoViewSet)
router.register(r'ships', views.ShipViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'engines', views.EngineViewSet)
router.register(r'resources', views.ResourceViewSet)
router.register(r'droids', views.DroidViewSet)
router.register(r'weapons', views.WeaponViewSet)
router.register(r'items_type', views.ItemTypeViewSet)

schema_view = get_swagger_view(title='StarWars API')

urlpatterns = [
    path('', include('main.urls')),
    path('wiki/', include('wiki.urls')),
    path('user/', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('shop/', include('shop.urls')),
    path('account/', include('personalAccount.urls')),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('drf/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
