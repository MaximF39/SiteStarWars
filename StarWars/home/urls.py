from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('registration', views.registration, name='registration'),
    # path('accounts/', include('django.contrib.auth.urls')),
]