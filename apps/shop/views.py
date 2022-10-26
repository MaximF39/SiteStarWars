from django.shortcuts import render
from .models import *


def shop(request):
    id_type = 0
    if request.method == 'POST':
        if request.POST['filter'] != 0:
            id_type = int(request.POST['filter'])

    items = BaseItems.objects.select_related('ammo', 'resources', 'engines', 'devices', 'weapons', 'droids', 'ships')
    filter = Type.objects.all().order_by('type')
    if id_type:
        items = items.filter(type=id_type)
    return render(request, 'shop/shop.html', context={'items': items, 'filter': filter, 'type': id_type})
