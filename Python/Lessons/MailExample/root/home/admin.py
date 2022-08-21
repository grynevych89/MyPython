from django.contrib import admin
from .models import UserEmail, Feedback, Mailing

admin.site.register(UserEmail)
admin.site.register(Feedback)
admin.site.register(Mailing)
