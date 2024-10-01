from django.db import models
from authorize.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField(null=True, blank=True)
    preparation = models.TextField(null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title