from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import CreateUserForm, ModifyUserForm
from .models import Users


class UserAdmin(BaseUserAdmin):
    form = ModifyUserForm
    add_form = CreateUserForm

    list_display = ("first_name", "last_name", "national_code", "is_active")
    list_filter = ("is_active",)
    search_fields = ("national_code", "postal_code")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "national_code",
                           "phone_number", "education", "home_address")}),

        ("Permissions", {"fields": ("is_active", "is_admin", "last_login")}),
    )

    add_fieldsets = (
        (None, {"fields": ("first_name", "last_name", "birth_date",
                           "national_code", "is_active", "home_address",
                           "postal_code", "register_date", "phone_number",
                           "education", "pass1", "pass2")})
    )

    ordering = ("national_code",)
    filter_horizontal = ()  # for permissions


admin.site.unregister(Group)
admin.site.register(Users, UserAdmin)
