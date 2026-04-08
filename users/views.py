from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .forms import ReaderRegistrationForm, AuthorRegistrationForm, ReaderLoginForm, AuthorLoginForm, UserProfileForm

User = get_user_model()

def reader_register(request):
    if request.method == 'POST':
        form = ReaderRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration successful! Please login.')
                return redirect('users:reader_login')
            except IntegrityError:
                form.add_error('email', 'A user with this email already exists. Please use a different email.')
    else:
        form = ReaderRegistrationForm()
    return render(request, 'users/reader_register.html', {'form': form})

def author_register(request):
    if request.method == 'POST':
        form = AuthorRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration successful! Please login.')
                return redirect('users:author_login')
            except IntegrityError:
                form.add_error('email', 'A user with this email already exists. Please use a different email.')
    else:
        form = AuthorRegistrationForm()
    return render(request, 'users/author_register.html', {'form': form})

def reader_login(request):
    if request.method == 'POST':
        form = ReaderLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_or_roll = form.cleaned_data['phone_or_roll']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(
                    user_type='reader',
                    email=email,
                )
                if user.get_full_name() == name:
                    if (user.phone_number == phone_or_roll or user.roll_no == phone_or_roll):
                        user = authenticate(request, username=user.username, password=password)
                        if user is not None:
                            login(request, user)
                            messages.success(request, f'Welcome {user.get_full_name()}!')
                            return redirect('books:dashboard')
                        else:
                            messages.error(request, 'Incorrect password.')
                    else:
                        messages.error(request, 'Phone/Roll number does not match.')
                else:
                    messages.error(request, 'Name does not match.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
    else:
        form = ReaderLoginForm()
    return render(request, 'users/reader_login.html', {'form': form})

def author_login(request):
    if request.method == 'POST':
        form = AuthorLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(
                    user_type='author',
                    email=email,
                )
                if user.get_full_name() == name and user.phone_number == phone_number:
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, f'Welcome {user.get_full_name()}!')
                        return redirect('books:author_dashboard')
                    else:
                        messages.error(request, 'Incorrect password.')
                else:
                    messages.error(request, 'Name or phone number does not match.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
    else:
        form = AuthorLoginForm()
    return render(request, 'users/author_login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('users:home')

def home(request):
    return render(request, 'users/home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})
