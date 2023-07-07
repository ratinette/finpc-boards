from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # 회원가입 성공 시 로그인 페이지로 이동
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # 로그인 성공 시 홈 페이지로 이동
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")  # 로그아웃 후 홈 페이지로 이동
