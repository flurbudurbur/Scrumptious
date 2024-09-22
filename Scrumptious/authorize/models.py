from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

