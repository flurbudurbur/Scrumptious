from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from authorize.forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def login_view(request):
    context = {}
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
    context['form'] = form
    return render(request, 'login.html', context)


def register_view(request):
    context = {}
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = request.POST.get('Confirm Password')
            if password == confirm_password:
                hashed_password = make_password(password)
                form.instance.password = hashed_password
                form.save()
                return render(request, 'home.html', context)
    context['form'] = form
    return render(request, 'register.html', context)
