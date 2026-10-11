# apps/matches/models/match_lineup.py

from django.db import models
from apps.core.base_models import ActiveModel
from apps.football.models.player_registration import PlayerRegistration
from .match import Match
from apps.core.choices import  SquadSelectionChoices, NotCalledReasonChoices
from django.core.exceptions import ValidationError


class MatchLineup(ActiveModel):
    """
    Players selected for a match.
    """
    match = models.ForeignKey(Match,on_delete=models.CASCADE,related_name="lineups",)
    player_registration = models.ForeignKey(PlayerRegistration,on_delete=models.PROTECT,related_name="match_lineups",)
    shirt_number = models.PositiveSmallIntegerField(blank=True, null=True)
    selection_type = models.CharField(max_length=30,choices=SquadSelectionChoices.choices,default=SquadSelectionChoices.STARTING,)
    not_called_reason = models.CharField(max_length=30, choices=NotCalledReasonChoices.choices, blank=True, null=True,)
    is_captain = models.BooleanField(default=False)

    class Meta:

        ordering = ["selection_type", "shirt_number",]

        constraints = [
            models.UniqueConstraint(
                fields=["match", "player_registration"],
                name="unique_player_in_match_lineup",
            )]

    def __str__(self):
        return f"{self.player_registration} - {self.match}"

    def clean(self):
        if self.selection_type == SquadSelectionChoices.NOT_CALLED:
            if not self.not_called_reason:
                raise ValidationError("A reason is required when the player is not called.")
        else:
            if self.not_called_reason:
                raise ValidationError(
                    "Not-called reason can only be used for players who were not called.")






