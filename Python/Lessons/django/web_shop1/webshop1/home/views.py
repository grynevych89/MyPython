from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', context={
        'page_name': 'Главная',
        'page_app': 'home',
        'page_view': 'index',
    })


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')

