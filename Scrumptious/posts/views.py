from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'home.html', context={'posts': Post.objects.all()})


def makepost(request):
    return render(request, 'makepost.html')