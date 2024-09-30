from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post
from .forms import MakePost

# Create your views here.

def home(request):
    return render(request, 'home.html', context={'posts': Post.objects.all()})


def makepost(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                ingredient=form.cleaned_data['ingredient'],
                preparation=form.cleaned_data['preparation'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                author=request.user
            )
            post.save()
            return render(request, 'home.html', context={'posts': Post.objects.all()})
    else:
        form = MakePost()
    return render(request, 'makepost.html')