from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    
    STATUS = (
        ('user', 'user'),
        ('admin', 'admin'),
        ('superadmin', 'superadmin'),
    )
    
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='user')
    description = models.TextField('description', max_length=600, default='', blank=True)
    
    def __str__(self):
        return self.username