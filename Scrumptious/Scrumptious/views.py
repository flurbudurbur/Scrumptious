from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

from posts.models import Post


# @login_required
def home_view(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html', {})

def career_view(request):
    return render(request, 'careers.html', {})