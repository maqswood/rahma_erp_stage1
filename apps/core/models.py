from django.conf import settings
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=180, unique=True)
    legal_name = models.CharField(max_length=240, blank=True)
    vat_registration_number = models.CharField(max_length=40, blank=True)
    default_currency = models.CharField(max_length=3, default="SAR")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    class Kind(models.TextChoices):
        HEAD_OFFICE = "HEAD_OFFICE", "Head Office"
        CENTRAL_SALES = "CENTRAL_SALES", "Central Sales Unit"
        WAREHOUSE = "WAREHOUSE", "Central Warehouse"
        RETAIL = "RETAIL", "Retail Branch"

    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="branches")
    code = models.CharField(max_length=24)
    name = models.CharField(max_length=180)
    kind = models.CharField(max_length=20, choices=Kind.choices, default=Kind.RETAIL)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["organization", "code"], name="uniq_branch_code_per_org"),
        ]
        indexes = [models.Index(fields=["organization", "is_active"])]

    def __str__(self):
        return f"{self.code} — {self.name}"

class AuditEvent(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.PROTECT)
    action = models.CharField(max_length=80)
    entity_type = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=80, blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Do not store passwords, secrets, payment credentials, or full sensitive document contents here.

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["entity_type", "entity_id"]), models.Index(fields=["created_at"])]
