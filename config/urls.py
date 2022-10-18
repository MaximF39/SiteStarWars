from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('shop/', include('shop.urls')),
    path('account/', include('personalAccount.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
