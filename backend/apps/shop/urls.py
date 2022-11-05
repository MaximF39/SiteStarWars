from django.urls import path, include

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', shop, name='shop'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

