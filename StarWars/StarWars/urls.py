from django.contrib import admin
from django.urls import include, path
import rest_framework
import djoser


urlpatterns = [
    path('', include('Main.urls')),
    path('', include('Accounts.urls')),
    path('forum/', include('Forum.urls')),
    path('shop/', include('Shop.urls')),
    path('account/', include('PersonalAccount.urls')),
    path('admin/', admin.site.urls),

    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]