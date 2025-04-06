"""accounts views."""

from django.shortcuts import render
from django.views import View
from accounts.models import UserModel
from django.contrib.auth import authenticate, login, logout


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
        return render(request, "accounts/registration_success.html", {"user": new_user})

    def get(self, request):
        """Render the registration page."""
        return render(request, "accounts/accounts_signup.html")


class UserLoginView(View):
    """View to handle user login."""

    def post(self, request):
        """Render the login page."""
        email = request.GET.get("email")
        password = request.GET.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "accounts/login_success.html", {"user": user})
        else:
            # Invalid login
            return render(
                request,
                "accounts/accounts_login.html",
                {"error": "Invalid credentials"},
            )

    def get(self, request):
        """Render the login page."""
        return render(request, "accounts/accounts_login.html")


class UserLogoutView(View):
    """View to handle user logout."""

    def get(self, request):
        """Handle user logout."""
        logout(request)
        return render(request, "accounts/logout.html")
