from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('recommends:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('recommends:index')
    else :
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('recommends:index')


def profile(request, username):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            # Profile.objects.create(user=user) #프로필 생성
            auth_login(request, user)
            return redirect('recommends:index')
    
    else:
        signup_form = CustomUserCreationForm()

    context = {
        'signup_form' : signup_form,
    }
    
    return render(request,'accounts/signup.html', context)
