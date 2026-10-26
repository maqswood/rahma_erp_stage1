from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Administrator"
        ACCOUNTANT = "ACCOUNTANT", "Head Office Accountant"
        PURCHASING_MANAGER = "PURCHASING_MANAGER", "Purchasing Manager"
        PURCHASER = "PURCHASER", "Purchaser"
        WAREHOUSE_MANAGER = "WAREHOUSE_MANAGER", "Warehouse Manager"
        BRANCH_MANAGER = "BRANCH_MANAGER", "Branch Manager"
        CASHIER = "CASHIER", "Cashier"
        AUDITOR = "AUDITOR", "Auditor / Read Only"

    role = models.CharField(max_length=24, choices=Role.choices, default=Role.CASHIER)
    preferred_language = models.CharField(max_length=5, choices=[("en", "English"), ("ar", "Arabic")], default="en")

class UserBranchAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="branch_access")
    branch = models.ForeignKey("core.Branch", on_delete=models.PROTECT, related_name="user_access")
    can_view = models.BooleanField(default=True)
    can_transact = models.BooleanField(default=False)
    can_approve = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "branch"], name="uniq_user_branch_access")]
        indexes = [models.Index(fields=["branch", "user"])]

    def __str__(self):
        return f"{self.user} — {self.branch}"
