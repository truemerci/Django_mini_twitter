from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(blank=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
