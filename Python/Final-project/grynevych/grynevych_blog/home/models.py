from django.db import models


# 1
class UserEmail(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.email)


# 2
class Feedback(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)
    user_email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.subject)


# 3
class Mailing(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)
    sent = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.subject)
