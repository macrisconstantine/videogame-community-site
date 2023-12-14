from django.db import models
from django.contrib.auth.models import AbstractUser

# Simple custom user and appropriate statuses created for the project
class CustomUser(AbstractUser):
    STATUS = (
        ('user','user'),
        ('admin','admin'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='user')
    description = models.TextField('Description', max_length=600, default='', blank=True)

    def __str__(self):
        return self.username
