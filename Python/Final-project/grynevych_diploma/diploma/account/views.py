from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html',)
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 1 - Валидация данных (на стороне сервера)...

        # 2 - Сохранение пользователя в базе
        user = User.objects.create_user(login_x, email_x, pass1_x)
        if user is None:
            mess = 'В регистрации отказано!'
            color = 'red'
        else:
            user.save()
            mess = 'Регистрация успешно завершена!'
            color = 'green'

        # 3 - Вывод отчета
        return render(request, 'account/report.html', context={
            'page_name': 'Отчет о регистрации',
            'page_app': 'account',
            'page_view': 'report',
            'mess': mess,
            'color': color,
        })


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html', context={
            'page_name': 'Авторизация',
            'page_app': 'account',
            'page_view': 'entry',
        })
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 - Проверка подлинности пары логин/пароль:
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            mess = 'Такого пользователя не существует!'
            color = 'red'
            return render(request, 'account/report.html', context={
                'page_name': 'Отчет об авторизации',
                'page_app': 'account',
                'page_view': 'report',
                'mess': mess,
                'color': color,
            })
        else:
            login(request, user)
            return redirect('/')


def sign_out(request):
    logout(request)
    return render(request, 'account/logout.html', context={
        'page_name': 'Выход',
        'page_app': 'account',
        'page_view': 'sign_out',
    })


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')
    try:
        User.objects.get(username=login_y)
        response['message'] = 'занят'
    except User.DoesNotExist:
        response['message'] = 'свободен'
    return JsonResponse(response)
