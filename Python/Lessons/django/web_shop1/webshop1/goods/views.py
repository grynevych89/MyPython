from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    size_const = 6
    all_products = Product.objects.all()

    paginator = Paginator(all_products, size_const)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'goods/index.html', context={
        'page_name': 'Каталог',
        'page_app': 'goods',
        'page_view': 'index',
        'products': page_obj,
    })
