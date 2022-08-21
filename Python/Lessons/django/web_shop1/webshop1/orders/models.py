from django.db import models
from django.contrib.auth.models import User
from goods.models import Product
from django.utils import timezone


class Order2(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)

