from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('newsletter', newsletter, name='newsletter'),
    path('contact', contact, name='contact'),
]
