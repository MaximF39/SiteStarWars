from django.shortcuts import render
from .models import *


def shop(request):
    if request.method == 'POST':
        if request.POST['filter'] != 0:
            id_type = int(request.POST['filter'])

    return render(request, 'shop/shop.html', context={'items': items, 'filter': filter, 'type': id_type})
