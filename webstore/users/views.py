from django.contrib.auth import logout as django_logout, \
    login as django_login, authenticate
from django.shortcuts import render, redirect
from users.forms import UserForm, LoginForm
from .models import Member
from django.http import HttpResponse


def login(request):
    login_form = LoginForm()
    context = {
        "my_form": login_form
    }
    return render(request, 'users/login.html', context)

def login_process(request):

    if request.method == 'POST':

        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # 이렇게 전달받은 username과 password를 이용해서 로그인 인증처리를 진행
        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)   # 로그인 처리
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 접속해 주세요!')


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
            login(request)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})