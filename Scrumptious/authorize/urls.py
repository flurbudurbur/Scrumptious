from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from authorize.forms import LoginForm


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout, name='logout'),
]