from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import MakePost

  
def makepost(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/posts/')
    return render(request, 'makepost.html', context={'form': MakePost})
