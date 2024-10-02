from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect, get_object_or_404

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


@login_required
def admin_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    elif User.is_authenticated and request.user.is_staff:
        users = User.objects.all()
        return render(request, 'admin/admin.html', {"users": users})
    else:
        return redirect_to_login(request.get_full_path(), 'login')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Get the user or show 404 if not found
    if request.method == 'POST':
        # Update user details based on form data
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.is_active = 'is_active' in request.POST  # Activate/deactivate user
        user.save()
        return redirect('admin')  # Redirect to the user list after saving changes
    return render(request, 'admin/edituser.html', {'user': user})

