from django.urls import path
from .views import index, newsletter, contact, success, failed

urlpatterns = [
    path('', index, name='index'),
    path('newsletter', newsletter, name='newsletter'),
    path('contact', contact, name='contact'),
    path('success', success, name='success'),
    path('failed', failed, name='failed'),
]
