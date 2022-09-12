from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from accounts.views import signup

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
