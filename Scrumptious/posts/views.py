from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from Scrumptious.forms import AddIngredient
from Scrumptious.models import Ingredients
from .forms import MakePost, CommentForm, LikeForm

from .models import Post, Comments, Bookmarks, Likes


def home_view(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        ingredients = request.POST.getlist('ingredients[]')
        for ingredient in ingredients:
            ingredient_form = AddIngredient({'name': ingredient, 'created_by': request.user})
            if not Ingredients.objects.filter(name=ingredient).exists() and ingredient_form.is_valid():
                ingredient_form.save()
        ingredient_ids = Ingredients.objects.filter(name__in=ingredients).values_list('id', flat=True)
        form.ingredients = ingredient_ids
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        ingredients = Ingredients.objects.all()
        form = MakePost()
        return render(request, 'makepost.html', context={'form': form, 'ingredients': ingredients})


def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comments.objects.filter(post_id=post)
    likes = Likes.objects.filter(post_id=post_id).count()
    bookmarks = Bookmarks.objects.filter(post_id=post_id).count()
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form, 'like_count': likes, 'bookmark_count': bookmarks}
    if request.method == 'POST':
        if request.POST.get('action') == 'like':
            form = LikeForm(request.POST)
            if form.is_valid():
                liked = Likes.objects.filter(user=request.user, post_id=post_id)
                if liked.exists():
                    liked.delete()
                    return redirect('post', post_id=post.id)
                like = form.save(commit=False)
                like.user = request.user
                like.post = post.id
                like.save()
                return redirect('post', post_id=post.id)
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('post', post_id=post.id)
    return render(request, 'post.html', context)
