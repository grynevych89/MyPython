from django.urls import path
from .views import index, about, contact, admin_page, newsletter, success, failed, video_page

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('admin_page', admin_page, name='admin_page'),
    path('newsletter', newsletter, name='newsletter'),
    path('success', success, name='success'),
    path('failed', failed, name='failed'),
    path('video_page', video_page, name='video_page'),
]
