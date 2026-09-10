from rest_framework.permissions import BasePermission

class OrganizationMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class OrganizationAdmin(OrganizationMember):
    allowed_roles = {"OWNER", "ADMIN"}

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.memberships.filter(
            organization = view.get_organization(),
            role__in = self.allowed_roles,
            is_active = True,
        ).exists()

class AnalystPermission(OrganizationMember):
    allowed_roles = {"OWNER", "ADMIN", "COACH", "ANALYST"}

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        organization = view.get_organization()
        return request.user.memberships.filter(
            organization = organization,
            role__in = self.allowed_roles,
            is_active = True,
        ).exists()

    