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

def admin_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'admin/admin.html', {"form": form})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Get the user or show 404 if not found
    if request.method == 'POST':
        # Update user details based on form data
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.is_active = 'is_active' in request.POST  # Activate/deactivate user
        user.is_staff = 'is_staff' in request.POST  # Activate/deactivate staff
        user.save()
        return redirect('admin_user_list')  # Redirect to the user list after saving changes
    return render(request, 'edit_user.html', {'user': user})