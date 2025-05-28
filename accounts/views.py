"""accounts views."""

from django.shortcuts import render, redirect
from django.views import View
from accounts.models import UserModel
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse


class UserRegistrationView(View):
    """View to handle user registration."""

    def post(self, request):
        """Handle user registration."""
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Here you would typically save the user to the database
        # and send a confirmation email.
        new_user = UserModel.objects.create_user(
            email=email, username=username, password=password
        )
        new_user.full_clean()
        new_user.save()
        # You can also send a confirmation email here
        # send_confirmation_email(new_user)
        return redirect("accounts:login")

    def get(self, request):
        """Render the registration page."""
        form = UserRegisterForm()
        return render(request, "accounts/signup.html", {"form": form})


class UserLoginView(View):
    """View to handle user login."""

    def post(self, request):
        """Render the login page."""
        form = UserLoginForm()
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = authenticate(request, email=email, password=password)
        try:
            if user is not None:
                print("User authenticated successfully.")
                login(request, user)
                return redirect(
                    "blogs:list"
                )  # Redirect to the blog list page after login
        except Exception as e:
            print(f"Error during authentication: {e}")

        return redirect("accounts:login")

    def get(self, request):
        """Render the login page."""
        form = UserLoginForm()
        return render(request, "accounts/login.html", {"form": form})


class UserLogoutView(View):
    """View to handle user logout."""

    def get(self, request):
        """Handle user logout."""
        logout(request)
        return redirect("home:home")


class UserProfileView(View):
    """View to handle user profile."""

    def get(self, request):
        """Render the user profile page."""
        user = request.user
        if not user.is_authenticated:
            return redirect("accounts:login")
        return render(request, "accounts/profile.html", {"user": user})


class PasswordResetView(View):
    """View to handle password reset."""

    def get(self, request):
        """Render the password reset page."""
        return render(request, "accounts/password_reset.html")

    def post(self, request):
        """Handle password reset logic."""
        email = request.POST.get("email")
        # Here you would typically send a password reset email
        # send_password_reset_email(email)
        return redirect("accounts:login")


class PasswordChangeView(View):
    """View to handle password change."""

    def get(self, request):
        """Render the password change page."""
        return render(request, "accounts/password_change.html")

    def post(self, request):
        """Handle password change logic."""
        user = request.user
        if not user.is_authenticated:
            return redirect("accounts:login")

        new_password = request.POST.get("new_password")
        user.set_password(new_password)
        user.save()
        return redirect("accounts:login")
