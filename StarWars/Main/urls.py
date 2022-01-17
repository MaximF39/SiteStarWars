from django.urls import path, include

from .views import *
#
urlpatterns = [
    path('', redirect_main),
    path('main/', main, name='main'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

