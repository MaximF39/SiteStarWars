from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import *
from . import models


class shop(ListView):
    model = BaseItems
    template_name = 'shop/shop.html'
    object_list = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        select_type = int(request.GET.get('item_type', 1))
        types = models.ItemsType.objects.all()
        en_name = types[select_type - 1].type_en
        if select_type == 1:
            items = models.BaseItems.objects.select_related('ammo', 'resources', 'engines', 'devices', 'weapons', 'droids', 'ships')
        else:
            items = getattr(models, en_name).objects.all()
        return render(request, self.template_name, context={'items': items, 'types': types, 'select_type': select_type})
