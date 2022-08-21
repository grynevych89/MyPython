from django.shortcuts import render
from django.http import JsonResponse
from .models import Order2


def index(request):
    orders = Order2.objects.filter(user_id=request.user.id)
    return render(request, 'orders/index.html', context={
        'page_name': 'Корзина',
        'page_app': 'orders',
        'page_view': 'cart',
        'orders': orders,
    })


def checkout(request):
    orders = Order2.objects.filter(user_id=request.user.id)
    return render(request, 'orders/checkout.html', context={
        'page_name': 'Заказы',
        'page_app': 'orders',
        'page_view': 'checkout',
        'orders': orders,
    })


def ajax_cart(request):
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')

    Order2.objects.create(
        title=f'Order-{pid}/{uid}',
        product_id=pid,
        user_id=uid,
        status='Ожидание подтверждения заказа'
    )

    user_orders = Order2.objects.filter(user_id=uid)
    cost = 0
    for order in user_orders:
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)


def ajax_cart_display(request):
    response = dict()
    uid = request.GET.get('uid')
    user_orders = Order2.objects.filter(user_id=uid)

    cost = 0
    for order in user_orders:
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)
