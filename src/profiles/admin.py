from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserBlog, Technology


class UserBlogAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "first_name", "last_name", "middle_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "gender", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Прочая информация"), {"fields": ("phone", "avatar",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")})

    )


admin.site.register(UserBlog, UserBlogAdmin)
admin.site.register(Technology)
