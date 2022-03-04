from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm, LoginForm
from .models import Member


def login(request):
    login_form = LoginForm()
    context = {
        "my_form": login_form
    }
    return render(request, 'users/login.html', context)

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})