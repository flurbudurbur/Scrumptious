from django.db.models import Count
from django.shortcuts import render

from posts.models import Post, Likes, Bookmarks


# @login_required
def home_view(request):
    posts = Post.objects.annotate(
        comment_count=Count('comments'))
    for post in posts:
        post.like_count = Likes.objects.filter(post_id=post.id).count()
        post.bookmark_count = Bookmarks.objects.filter(post_id=post.id).count()
    context = {'posts': posts}
    return render(request, 'home.html', context)


def about_view(request):
    return render(request, 'about.html', {})


def career_view(request):
    return render(request, 'careers.html', {})
