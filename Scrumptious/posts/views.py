from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MakePost, CommentForm, AddIngredient
from .models import Post, Comments, Bookmarks, Likes, PostIngredients, Ingredients

def home_view(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts
    context = {
        'posts': posts,
    }
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
                like.delete()  # User unlikes the post
            return redirect('post', post_id=post.id)

        elif request.POST.get('action') == 'bookmark':
            bookmark, created = Bookmarks.objects.get_or_create(user=request.user, post=post)
            if not created:
                bookmark.delete()  # User removes the bookmark
            return redirect('post', post_id=post.id)

        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('post', post_id=post.id)

    # Prepare data for rendering the post view
    ingredients = PostIngredients.objects.filter(post_id=post_id).values_list('ingredient__name', flat=True)
    comments = Comments.objects.filter(post=post)
    likes = Likes.objects.filter(post=post).count()
    bookmarks = Bookmarks.objects.filter(post=post).count()
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

from .models import Post, Bookmarks

@login_required
def profile_view(request):
    # Get all posts created by the current user
    user_posts = Post.objects.filter(user=request.user)

    # Get all posts bookmarked by the current user
    bookmarked_posts = Post.objects.filter(bookmarked_posts__user=request.user)

    context = {
        'user': request.user,
        'posts': user_posts,
        'bookmarked_posts': bookmarked_posts,
    }
    return render(request, 'profile.html', context)

