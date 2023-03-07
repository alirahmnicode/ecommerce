from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


def user_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ثبت نام با موفقیت انجام شد.")
            return redirect("inventory:index")
        messages.error(request, "هنگام ثبت نام خطایی رخ داد.")
    form = CustomUserCreationForm()
    return render(request, "account/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd.get("username")
            password = cd.get("password")
            user = authenticate(phone=phone, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "با موفقیت وارد حساب کاربری خود شدید.")
                return redirect("inventory:index")
            else:
                messages.error(request, "پسورد یا شماره تماس اشتباه است.")

        else:
            messages.error(request, "خطایی رخ داد مجددا تلاش کنید.")
    form = AuthenticationForm()
    return render(request, "account/login.html", {"form": form})


def user_logout(request):
    pass
