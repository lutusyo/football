from django.db import models

from apps.core.base_models import ActiveModel
from apps.organizations.models import Organization

from .player_profile import PlayerProfile


class Contract(ActiveModel):
    """
    Represents a contractual agreement between
    an organization and a player.
    """
    player = models.ForeignKey(PlayerProfile,on_delete=models.CASCADE,related_name="contracts",)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="contracts",)
    start_date = models.DateField()
    end_date = models.DateField()
    contract_number = models.CharField(max_length=100,blank=True,)
    is_professional = models.BooleanField(default=True,)
    is_current = models.BooleanField(default=True,)
    notes = models.TextField(blank=True,)

    class Meta:
        ordering = ["-start_date",]

    def __str__(self):
        return (f"{self.player.person.full_name}"f" ({self.organization.short_name})")