from django.db import models
from django.conf import settings
from apps.core.base_models import ActiveModel
from ...organizations.models import Organization


class Membership(ActiveModel):

    class RoleChoices(models.TextChoices):
        OWNER = "OWNER", "Owner"
        ADMIN = "ADMIN", "Admin"
        COACH = "COACH", "Coach"
        ANALYST = "ANALYST", "Analyst"
        MEDICAL = "MEDICAL", "Medical"
        PLAYER = "PLAYER", "Player"
        VIEWER = "VIEWER", "Viewer"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'organization'], name="unique_user_orgnization")
        ]

    def __str__(self):
        return f"{self.user} {self.organization} ({self.role})"
