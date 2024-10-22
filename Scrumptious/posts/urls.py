from django.urls import path

from .views import home_view, create_post_view, post_view, profile_view

urlpatterns = [
    #path('', home_view, name='home'),
    path('create/', create_post_view, name='create'),  # Ensure this line is present
    path('post/<int:post_id>/', post_view, name='post'),
    path('profile/', profile_view, name='profile'),
]
