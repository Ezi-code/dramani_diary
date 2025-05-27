from django.contrib import admin
from accounts.models import UserModel

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """Admin view for UserModel."""

    list_display = ("email", "username", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "username")
    list_filter = ("is_active", "is_staff", "is_superuser")


admin.site.register(UserModel, UserProfileAdmin)
