from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.accounts.permissions import accessible_branches
from .models import Branch

@login_required
def dashboard(request):
    allowed = accessible_branches(request.user)
    branches = Branch.objects.filter(is_active=True)
    if allowed is not None:
        branches = branches.filter(pk__in=allowed)
    # Stage 1 intentionally shows no fabricated financial metrics.
    return render(request, "core/dashboard.html", {"branches": branches})
