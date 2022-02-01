from django.urls import path, include

from .views import *
#
urlpatterns = [
    path('', redirect_main),
    path('main/', main, name='main'),
    path('faq/', faq, name='faq'),
    path('news/', news, name='news'),
    path('top/', top, name='top'),
]

