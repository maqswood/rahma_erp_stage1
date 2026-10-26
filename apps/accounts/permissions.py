from django.core.exceptions import PermissionDenied
from .models import UserBranchAccess

def accessible_branches(user, *, transact=False):
    """Return only branches this user may access; use in every branch-scoped queryset."""
    if not user.is_authenticated:
        return UserBranchAccess.objects.none().values_list("branch_id", flat=True)
    if user.is_superuser or user.role == user.Role.SUPER_ADMIN:
        return None  # Caller must explicitly handle None as unrestricted.
    qs = UserBranchAccess.objects.filter(user=user, can_view=True)
    if transact:
        qs = qs.filter(can_transact=True)
    return qs.values_list("branch_id", flat=True)

def require_branch_access(user, branch_id, *, transact=False):
    ids = accessible_branches(user, transact=transact)
    if ids is not None and not ids.filter(pk=branch_id).exists():
        raise PermissionDenied("You do not have permission for this branch.")
    return True
