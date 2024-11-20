import password
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegister


def sign_up_by_html(request):
    users = ['ivan', 'mikhail', 'nikolay', 'oleg']
    info = {}

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) > 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}')
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) <= 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['ivan', 'mikhail', 'nikolay', 'oleg']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) > 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) <= 18:
                    info['error'] = 'Вы должны быть старше 18'
                elif username in users:
                    info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', context=info)
