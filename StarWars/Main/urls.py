from django.urls import path, include

from .views import *

urlpatterns = [

    path('player/create/', PlayerCreateView.as_view()),
    path('all/', PlayerListView.as_view()),
    path('player/detail/<int:pk>/', PlayerDetailView.as_view()),
    # path('', redirect_main),
    # path('main/', main, name='main'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user, name='logout'),
    # path('faq/', faq, name='faq'),
    # path('news/', news, name='news'),
]

