from django.urls import path
from .views import ajax_cart, index, checkout, ajax_cart_display

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('checkout', checkout),
    path('ajax_cart_display', ajax_cart_display),
]
