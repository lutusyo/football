from django.core.exceptions import ValidationError
from django.db import models

from apps.core.base_models import ActiveModel
from apps.core.choices import MatchPeriodChoices
from apps.reference.models import Position
from .match_lineup import MatchLineup


class MatchAppearance(ActiveModel):
    lineup = models.OneToOneField(
        MatchLineup, on_delete=models.CASCADE, related_name="appearance"
    )
    position = models.ForeignKey(
        Position, on_delete=models.PROTECT, related_name="match_appearances"
    )
    entered_period = models.CharField(max_length=4, choices=MatchPeriodChoices.choices)
    entered_second = models.PositiveSmallIntegerField(default=0)
    exited_period = models.CharField(
        max_length=4, choices=MatchPeriodChoices.choices, blank=True, null=True
    )
    exited_second = models.PositiveSmallIntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    is_player_of_match = models.BooleanField(default=False)

    PERIOD_OFFSETS = {
        "1H": 0,
        "2H": 45 * 60,
        "ET1": 90 * 60,
        "ET2": 105 * 60,
        "PEN": 120 * 60,
    }

    def clean(self):
        if self.exited_period and self.exited_second is not None:
            entered = self.PERIOD_OFFSETS[self.entered_period] + self.entered_second
            exited = self.PERIOD_OFFSETS[self.exited_period] + self.exited_second

            if exited < entered:
                raise ValidationError("Exit time cannot be before entry time.")

    @property
    def minutes_played(self):
        if self.exited_period is None or self.exited_second is None:
            return None

        entered = self.PERIOD_OFFSETS[self.entered_period] + self.entered_second
        exited = self.PERIOD_OFFSETS[self.exited_period] + self.exited_second

        return round((exited - entered) / 60)

    class Meta:
        ordering = ["entered_period"]

    def __str__(self):
        return f"{self.lineup.player_registration.player.person.full_name} ({self.lineup.match})"