from django.db.models import Count
from django.shortcuts import render

from posts.models import Post, Likes, Bookmarks


# @login_required
def home_view(request):
    posts = Post.objects.annotate(
        comment_count=Count('comments'),
        like_count=Count('likes'),
        bookmark_count=Count('bookmarks'))
    context = {'posts': posts}
    return render(request, 'home.html', context)


def about_view(request):
    return render(request, 'about.html', {})


def career_view(request):
    return render(request, 'careers.html', {})
