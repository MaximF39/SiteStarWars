from django.urls import path, include

from .views import *

urlpatterns = [
    path('', account, name="account"),
    path('skills/', skills, name="skills"),
    path('angar/', angar, name="angar"),
    path('repository/', repository, name="repository"),
    path('clan_repository/', clan_repository, name="clan_repository"),
    path('inventory/', inventory, name="inventory"),
    path('character/', character, name="character"),
]