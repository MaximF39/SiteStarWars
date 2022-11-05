from django.shortcuts import render
from . import models


def shop(request):
    types = models.ItemsType.objects.all()
    select_type = int(request.GET.get('item_type', 1))
    en_name = types[select_type - 1].type_en
    if select_type == 1:
        items = models.BaseItems.objects.select_related('ammo', 'resources', 'engines', 'devices', 'weapons', 'droids', 'ships')
    else:
        items = getattr(models, en_name).objects.all()
    return render(request, 'shop/shop.html', context={'items': items, 'types': types, 'select_type': select_type})
