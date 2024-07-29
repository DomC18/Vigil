from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm
import globalvariables as gv

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            gv.current_user = username
            print()
            print(f"Active User(name): {gv.current_user}")
            print()
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            gv.current_user = username
            print()
            print(f"Active User(name): {gv.current_user}")
            print()
            return redirect('home')
        else:
            messages.error(request, 'Registration failed!')
            return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})