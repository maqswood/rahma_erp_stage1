from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserBranchAccess

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Rahma ERP", {"fields": ("role", "preferred_language")}),)
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

@admin.register(UserBranchAccess)
class UserBranchAccessAdmin(admin.ModelAdmin):
    list_display = ("user", "branch", "can_view", "can_transact", "can_approve")
    list_filter = ("branch", "can_view", "can_transact", "can_approve")
    search_fields = ("user__username", "branch__name", "branch__code")
