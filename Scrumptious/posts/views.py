from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from Scrumptious.forms import AddIngredient
from Scrumptious.models import Ingredients
from .forms import MakePost, CommentForm, LikeForm

from .models import Post, Comments, Bookmarks, Likes, PostIngredients


def home_view(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        ingredients = request.POST.getlist('ingredients-ls')
        for ingredient in ingredients:
            ingredient_form = AddIngredient({'name': ingredient, 'created_by': request.user})
            if not Ingredients.objects.filter(name=ingredient).exists() and ingredient_form.is_valid():
                ingredient_form.save()
        ingredient_ids = Ingredients.objects.filter(name__in=ingredients).values_list('id', flat=True)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for ingredient_id in ingredient_ids:
                PostIngredients.objects.create(post=post, ingredient_id=ingredient_id)
            return redirect('home')
        else:
            print(form.errors)
    ingredient_list = Ingredients.objects.all()
    form = MakePost()
    return render(request, 'makepost.html', context={'form': form, 'ingredients_list': ingredient_list})


def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        if request.POST.get('action') == 'like':
            like, created = Likes.objects.get_or_create(user=request.user, post=post)
            if not created:
                like.delete()
            else:
                like.liked = True
                like.save()
            return redirect('post', post_id=post.id)
        elif request.POST.get('action') == 'bookmark':
            bookmark, created = Bookmarks.objects.get_or_create(user=request.user, post=post)
            if not created:
                bookmark.delete()
            else:
                bookmark.bookmarked = True
                bookmark.save()
            return redirect('post', post_id=post.id)
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('post', post_id=post.id)
    ingredients = PostIngredients.objects.filter(post_id=post_id).values_list('ingredient__name', flat=True)
    comments = Comments.objects.filter(post_id=post)
    likes = Likes.objects.filter(post_id=post_id).count()
    bookmarks = Bookmarks.objects.filter(post_id=post_id).count()
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'like_count': likes,
        'bookmark_count': bookmarks,
        'ingredients': ingredients
    }
    return render(request, 'post.html', context)
