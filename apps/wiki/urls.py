from django.urls import path, include

from .views import *
#
urlpatterns = [
    path('', wiki, name='wiki'),
]

