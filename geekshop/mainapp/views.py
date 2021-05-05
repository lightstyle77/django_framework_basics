import os
import json

from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator

dir = os.path.dirname(__file__)



def index(request):
    context = {
        'title': 'GeekShop',
        'name_shop': 'GeekShop Store',
        'start_buy': 'Начать покупки',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('-price')
    else:
        products = Product.objects.all().order_by('-price')
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)
