
from django.urls import path, include

from config.urls import router
from users import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
