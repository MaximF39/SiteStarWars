from django.shortcuts import render
from . import models


def shop(request):
    if request.method == 'POST' and int(request.POST['filter']) != 8:
        id_type = int(request.POST['filter'])
        en_name = models.ItemsType.objects.values_list('type_en', flat=True).get(id=id_type)
        items = getattr(models, en_name).objects.all()
    else:
        id_type = 8
        items = models.BaseItems.objects.select_related('ammo', 'resources', 'engines', 'devices', 'weapons', 'droids', 'ships')
    filter = models.ItemsType.objects.all()
    return render(request, 'shop/shop.html', context={'items': items, 'filter': filter, 'type': id_type})
