from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


def user_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ثبت نام با موفقیت انجام شد.")
            return redirect("inventory:index")
        messages.error(request, "هنگام ثبت نام خطایی رخ داد.")
    form = CustomUserCreationForm()
    return render(request, "account/signup.html", {"form": form})


def user_login(request):
    pass


def user_logout(request):
    pass
