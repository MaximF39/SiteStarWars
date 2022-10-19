from django.shortcuts import render
from .models import *


def shop(request):
    items = BaseItems.objects.select_related('ammo', 'resources', 'ships', 'engines', 'devices', 'weapons', 'droids')
    return render(request, 'shop/shop.html', context={'items': items})
