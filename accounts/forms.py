from django import forms
from django.forms import ModelForm
from .models import UserModel


class UserRegisterForm(ModelForm):
    """user registration form."""

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password"}, render_value=False
        ),
    )

    class Meta:
        model = UserModel
        fields = ["email", "username", "password"]
        widgets = {
            "password": forms.PasswordInput(
                attrs={"placeholder": "Password"}, render_value=False
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
        }

    def clean(self):
        """validate the form data."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        """save the form data."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """user login form."""

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}, render_value=False
        ),
    )

    def clean(self):
        """validate the form data."""
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if not email or not password:
            raise forms.ValidationError("Email and Password are required.")
        return cleaned_data
