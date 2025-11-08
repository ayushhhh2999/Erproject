from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserCreationRequest, Dashboard, DashboardCreationRequest,PersonalDetail,Attendance


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "role",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "username")
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)


# ✅ FIXED: All classes at the same level, not nested
@admin.register(UserCreationRequest)
class UserCreationRequestAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "requested_by", "status", "created_at")
    list_filter = ("status", "role", "created_at")
    search_fields = ("username", "email", "requested_by__username")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description", "created_by__username")
    readonly_fields = ("created_at", "updated_at")


@admin.register(DashboardCreationRequest)
class DashboardCreationRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "requested_by", "status", "dashboard", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "requested_by__username")
    readonly_fields = ("created_at", "updated_at")


@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone",
        "department",
        "designation",
        "classroom",  # ✅ shows classroom column
        "is_active",
        "updated_at",
    )
    list_filter = (
        "is_active",
        "department",
        "designation",
        "classroom",  # ✅ filter by classroom
    )
    search_fields = ("user__username", "user__email", "phone", "department")
    ordering = ("-updated_at",)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "date",
        "status",
        "check_in",
        "check_out",
        "recorded_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("user__email", "recorded_by__email", "date", "status")
    list_filter = ("status", "date", "created_at")
    readonly_fields = ("created_at", "updated_at")    