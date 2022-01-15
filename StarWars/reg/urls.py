from django.urls import path, include

from .views import *
#
urlpatterns = [
    path('reg', registration, name='reg'),
     #path('accounts/', include('django.contrib.auth.urls')),
]

