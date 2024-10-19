from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)