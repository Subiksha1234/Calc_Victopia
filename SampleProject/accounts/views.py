from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def register(request):
    if request.method == 'POST': 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'travello/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'travello/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return render(request, 'travello/register.html')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, 'User created successfully!')
        return redirect('login')
    else:
        return render(request, 'travello/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'travello/login.html')
    else:
        return render(request, 'travello/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')