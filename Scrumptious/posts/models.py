from django.db import models
from django.contrib.auth.models import User
from Scrumptious.models import Ingredients

class Post(models.Model):
    title = models.CharField(max_length=100)
    preparation = models.TextField(null=True, blank=True)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    bookmarks = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostIngredients(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)  # Ensure this is the right import

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    liked = models.BooleanField(default=0)

from .models import Post

class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="bookmarked_posts")
    bookmarked = models.BooleanField(default=True)  # This can be optional based on your requirements

