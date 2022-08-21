from django.db import models


class Post(models.Model):
    """ Модель сообщения в ленте новостей """
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    content = models.TextField(max_length=1024)
    author = models.CharField(max_length=100)
    picture = models.FileField(upload_to='pictures/', null=True)
    publish = models.DateTimeField(auto_now_add=True)
    source = models.URLField()

    def __str__(self) -> str:
        return str(self.title)
