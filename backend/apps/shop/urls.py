from django.urls import path, include

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('1', redirect_shop),
    path('', Shop.as_view(), name='shop'),
    path('<slug:item_slug>', ShopFilter.as_view(), name='shop_filter'),
]

