"""accounts urls."""

from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("signup/", views.UserRegistrationView.as_view(), name="signup"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
]
