from django.shortcuts import render
from django.views.generic import TemplateView


import requests



def main_page(request):
    name = 'Все игры.ру'

    context = {
        'name': name
    }
    return render(request, 'main_page.html', context)


def shop_page(request):
    name = 'Магазин'
    game1 = 'Atomic Herat'
    game2 = 'Cyberpunk'
    game3 = 'PayDay'
    context = {
        'name': name,
        'game1': game1,
        'game2': game2,
        'game3': game3,


    }
    return render(request, 'shop.html', context)


def basket_page(request):
    X_API_KEY = '7CwbabvMoAHHpqP1VthjiA==MAelWFXPxQ04kAXX'
    URL = 'https://api.api-ninjas.com/v1/jokes'
    headers = {'X-API-KEY': X_API_KEY}
    response = requests.get(URL, headers=headers)
    data = response.json()
    joke = data[0].get('joke')
    context = {
        'joke': joke
    }
    return render(request, 'basket.html', context)