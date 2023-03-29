from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from .forms import CustomAuthenticationForm, CustomUserCreationForm, ProfileUpdateForm


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
        form = CustomAuthenticationForm(request, data=request.POST)
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
    form = CustomAuthenticationForm(request=None)
    return render(request, "account/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "با موفقیت از حساب کاربری خارج شدید.")
    return redirect("inventory:index")


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile_form = ProfileUpdateForm(instance=user.profile)
        context = {
            "user": user,
            "profile_form": profile_form,
        }
        return render(request, "account/profile/profile.html", context)


class UpdateProfileView(View):
    def post(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            form = ProfileUpdateForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("user:profile")
            else:
                return redirect(request.META.get("HTTP_REFERER"))
        except ObjectDoesNotExist:
            return HttpResponse("Exception: Data not found")
