from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Optional if you need a role

        try:
            # Create a new user
            user = User.objects.create_user(username=username, password=password, role=role)
            return render(request, 'register.html', {'message': 'User registered successfully!', 'message_type': 'success'})
        except IntegrityError:
            # Handle duplicate username
            return render(request, 'register.html', {'message': 'Username already exists. Please choose a different one.', 'message_type': 'error'})

    return render(request, 'register.html')


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.role = request.POST['role']
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('admin_dashboard')
    return render(request, 'edit_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('admin_dashboard')


@login_required
def add_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists!")
        else:
            User.objects.create_user(username=username, email=email, password=password, role=role)
            messages.success(request, "User added successfully!")
        return redirect('admin_dashboard')
    return render(request, 'add_user.html')
# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == "admin":
                return redirect('admin_dashboard')
            elif user.role == "moderator":
                return redirect('moderator_dashboard')
            elif user.role == "user":
                return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboards
@login_required
def admin_dashboard(request):
    if request.user.role != "admin":  # Replace with your custom role check if applicable
        return redirect('login')  # Only allow admins to access this dashboard
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'admin_dashboard.html', {'users': users})

@login_required
def moderator_dashboard(request):
    if request.user.role != 'moderator':
        return redirect('login')
    return render(request, 'moderator_dashboard.html')

@login_required
def user_dashboard(request):
    if request.user.role != 'user':
        return redirect('login')
    return render(request, 'user_dashboard.html')
