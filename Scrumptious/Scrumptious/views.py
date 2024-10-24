from django.db.models import Count
from django.shortcuts import render
from django.core.paginator import Paginator

from posts.models import Post, Likes, Bookmarks, Comments, PostIngredients
from django.db.models import Q


def home_view(request):
    query = request.GET.get('values')
    if query:
        posts = Post.objects.filter(
            Q(postingredients__ingredient__name__icontains=query) | Q(title__icontains=query)
        ).distinct().order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        post.like_count = Likes.objects.filter(post_id=post.id).count()
        post.bookmark_count = Bookmarks.objects.filter(post_id=post.id).count()
        post.comment_count = Comments.objects.filter(post_id=post.id).count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
               'query': query,
               }
    return render(request, 'home.html', context)


def about_view(request):
    return render(request, 'about.html', {})


def career_view(request):
    return render(request, 'careers.html', {})
