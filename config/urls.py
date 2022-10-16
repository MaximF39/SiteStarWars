from django.contrib import admin
from django.urls import include, path
import rest_framework
import djoser


urlpatterns = [
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('shop/', include('shop.urls')),
    path('account/', include('personalAccount.urls')),
    path('admin/', admin.site.urls),

    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]
