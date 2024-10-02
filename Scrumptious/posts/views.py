from django.shortcuts import render, redirect
from .forms import MakePost
from django.contrib.auth.models import User


def home_view(request):
    context = {}
    return render(request, 'home.html', context)

# @login_required
def makepost(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = MakePost()
    return render(request, 'makepost.html', context={'form': form})
