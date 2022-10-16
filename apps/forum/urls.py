from django.urls import path, include

from .views import *
#
urlpatterns = [
    path('', forum, name='forum'),
]