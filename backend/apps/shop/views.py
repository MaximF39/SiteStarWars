from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from . import models


class Shop(ListView):
    paginate_by = 10
    template_name = 'shop/shop.html'
    context_object_name = 'items'
    object_list = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = models.ItemsType.objects.all()
        select_type = 1
        context['select_type'] = select_type
        context['types'] = types
        return context

    def get_queryset(self):
        model = BaseItems.objects.all().order_by('id')
        return model


class ShopFilter(ListView):
    paginate_by = 10
    template_name = 'shop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = models.ItemsType.objects.all()
        select_type = int(self.kwargs['item_slug'])
        context['select_type'] = select_type
        context['types'] = types
        return context

    def get_queryset(self):
        select_type = int(self.kwargs['item_slug'])
        types = models.ItemsType.objects.all()
        en_name = types[select_type - 1].type_en
        model_items = getattr(models, en_name).objects.all().order_by('id')
        return model_items


def redirect_shop(request):
    return redirect('shop')