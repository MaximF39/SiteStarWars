from django.contrib import admin
from django.urls import include, path
import rest_framework
import djoser

urlpatterns = [
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/main/', include('Main.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
    # path('', include('Main.urls')),
    # path('forum/', include('Forum.urls')),
    # path('account/', include('PersonalAccount.urls')),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]