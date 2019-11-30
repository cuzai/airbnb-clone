from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# admin.site.register(models.User, CustomUserAdmin) == decorator below
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
