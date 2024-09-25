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
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                form.save()
        else:
            context['error'] = 'Passwords do not match.'
    context['form'] = form
    return render(request, 'register.html', context)