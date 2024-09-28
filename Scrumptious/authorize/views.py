from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from authorize.forms import RegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {"form": form})