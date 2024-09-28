from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from authorize.forms import UserLoginForm, UserRegistrationForm
from authorize.models import Users


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Error :(")
            return redirect('login')
    else:
        v_context = {}
        form = UserLoginForm()
        v_context['form'] = form
        return render(request, 'login.html', v_context)
# Create your views here.
# def login_view(request):
#     view_context = {}
#     form = UserLoginForm()
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             try:
#                 user = Users.objects.get(username=username)
#                 if check_password(password, user.password):
#                     login(request, user)
#                     return render(request, 'home.html', view_context)
#                 else:
#                     view_context['error'] = 'Invalid password.'
#             except Users.DoesNotExist:
#                 view_context['error'] = 'User does not exist.'
#     view_context['form'] = form
#     return render(request, 'login.html', view_context)


def register_view(request):
    view_context = {}
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        user = Users.objects.create
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = request.POST.get('Confirm Password')
            if password == confirm_password:
                hashed_password = make_password(password)
                form.instance.password = hashed_password
                user = form.save()
                login(request, user)
                return render(request, 'home.html', view_context)
    view_context['form'] = form
    return render(request, 'register.html', view_context)
#
# def logout_view(request):
#     logout(request)
#
#     return redirect('home')