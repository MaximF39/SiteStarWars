from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from shop import views

router = routers.DefaultRouter()


schema_view = get_swagger_view(title='StarWars API')

urlpatterns = [
    path('', include('main.urls')),
    path('wiki/', include('wiki.urls')),
    path('user/', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('shop/', include('shop.urls')),
    path('account/', include('personal_account.urls')),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api2/', include('drf_registration.urls')),
    path('drf/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
