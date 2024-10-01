from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import MakePost
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html', context={'posts': Post.objects.all()})


def makepost(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = "test"
            post.save()
            return redirect('/posts/')
    else:
        form = MakePost()
    return render(request, 'makepost.html', context={'form': MakePost()})





