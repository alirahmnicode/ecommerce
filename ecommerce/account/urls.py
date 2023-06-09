from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/", views.UpdateProfileView.as_view(), name="profile_update"),
]
