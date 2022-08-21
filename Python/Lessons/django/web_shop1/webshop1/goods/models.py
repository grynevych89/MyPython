from django.db import models
from producers.models import Producer
from categories.models import Category


class Product(models.Model):

    title = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    picture = models.FileField(upload_to='pictures/')
    price = models.FloatField()
    amount = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)
