from django.shortcuts import render
from .models import Post


def index(request):
    all_posts = Post.objects.all()
    return render(request, 'news/index.html', context={
        'page_title': 'Главная',
        'all_posts': all_posts
    })
