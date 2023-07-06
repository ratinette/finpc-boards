from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # 회원가입 성공 시 로그인 페이지로 이동
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})
