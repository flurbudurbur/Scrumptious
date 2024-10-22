from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scrumptious_ingredients')

    def __str__(self):
        return self.name