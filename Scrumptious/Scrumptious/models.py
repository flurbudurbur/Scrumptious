from django.db import models
from authorize.models import Users


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField(null=True, blank=True)
    preparation = models.TextField(null=True, blank=True)
    description = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)