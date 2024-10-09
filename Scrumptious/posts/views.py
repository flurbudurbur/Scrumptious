from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MakePost, CommentForm

from .models import Post, Comments


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


@login_required
def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comments.objects.filter(post_id=post)
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post', post_id=post.id)
    return render(request, 'post.html', context)