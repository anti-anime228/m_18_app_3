from django.shortcuts import render
from django.views.generic import TemplateView

import requests


def views1(request):
    return render(request, 'func_template.html')


class views2(TemplateView):
    template_name = 'class_template.html'


def main_page(request):
    name = 'Все игры.ру'

    context = {
        'name': name
    }
    return render(request, 'main_page.html', context)


def shop_page(request):
    name = 'Магазин'
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay"], 'name': name}

    return render(request, 'shop.html', context)


def basket_page(request):
    return render(request, 'basket.html')
