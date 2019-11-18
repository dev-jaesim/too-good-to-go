from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "state",
                    "business_owner",
                    "login_method",
                    "email_verified",
                    "email_secret",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("business_owner", "state")

    list_display = (
        "username",
        "state",
        "business_owner",
        "email_verified",
        "email_secret",
        "login_method",
    )

