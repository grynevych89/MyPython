from django.urls import path
from .views import register, entry, sign_out, ajax_reg

urlpatterns = [
    path('register', register),
    path('entry', entry),
    path('logout', sign_out),
    path('ajax_reg', ajax_reg),
]
