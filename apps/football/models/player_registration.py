from django.db import models

from apps.core.base_models import ActiveModel
from apps.core.choices import (
    RegistrationStatusChoices,
    RegistrationTypeChoices,
)
from apps.organizations.models import Organization
from .player_profile import PlayerProfile
from .season import Season
from .team import Team


class PlayerRegistration(ActiveModel):
    """
    Registers a player with a team for a specific season.
    """
    player = models.ForeignKey(PlayerProfile,on_delete=models.CASCADE,related_name="registrations",)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="player_registrations",)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="player_registrations",)
    season = models.ForeignKey(Season,on_delete=models.PROTECT,related_name="player_registrations", )
    squad_number = models.PositiveSmallIntegerField(blank=True,null=True,)
    registration_type = models.CharField(max_length=20,choices=RegistrationTypeChoices.choices,default=RegistrationTypeChoices.PERMANENT,)
    status = models.CharField(max_length=20,choices=RegistrationStatusChoices.choices,default=RegistrationStatusChoices.ACTIVE,)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True,)
    notes = models.TextField(blank=True,)
    is_current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date",]

        constraints = [
            models.UniqueConstraint(
                fields=["player","organization","team","season",],
                name="unique_player_team_season",
            )
        ]

    def __str__(self):
        return (f"{self.player.person.full_name}"f" - {self.team.name}" f" ({self.season.name})")