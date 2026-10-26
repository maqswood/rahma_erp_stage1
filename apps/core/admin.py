from django.contrib import admin
from .models import Organization, Branch, AuditEvent

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "default_currency", "is_active")
    search_fields = ("name", "legal_name")

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "kind", "organization", "is_active")
    list_filter = ("kind", "organization", "is_active")
    search_fields = ("code", "name")

@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ("created_at", "actor", "branch", "action", "entity_type", "entity_id")
    list_filter = ("action", "entity_type", "branch")
    search_fields = ("entity_id", "summary", "actor__username")
    readonly_fields = ("actor", "branch", "action", "entity_type", "entity_id", "summary", "created_at")
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
