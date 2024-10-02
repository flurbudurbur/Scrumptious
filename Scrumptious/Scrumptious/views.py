from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from posts.models import Post


# @login_required
def home_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html', {})

def career_view(request):
    return render(request, 'careers.html', {})