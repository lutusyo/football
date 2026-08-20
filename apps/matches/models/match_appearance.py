from django.db import models
from django.core.exceptions import ValidationError

from apps.core.base_models import ActiveModel
from apps.reference.models import Position
from .match_lineup import MatchLineup
from apps.core.choices import MatchPeriodChoices


class MatchAppearance(ActiveModel):
    """
    Represents a player's actual participation in a match.
    """

    lineup = models.OneToOneField(
        MatchLineup,
        on_delete=models.CASCADE,
        related_name="appearance",
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="match_appearances",
    )

    entered_period = models.CharField(
        max_length=4,
        choices=MatchPeriodChoices.choices,
    )

    entered_second = models.PositiveSmallIntegerField(
        default=0,
    )

    exited_period = models.CharField(
        max_length=4,
        choices=MatchPeriodChoices.choices,
        blank=True,
        null=True,
    )

    exited_second = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
    )

    is_player_of_match = models.BooleanField(
        default=False,
    )

    def clean(self):
        if (
            self.exited_second is not None
            and self.exited_second < self.entered_second
        ):
            raise ValidationError(
                "Exit time cannot be before entry time."
            )

    def minutes_played(self):
        if self.exited_second is None:
            return None

        return round(
            (self.exited_second - self.entered_second) / 60
        )

    class Meta:
        ordering = ["entered_period"]

    def __str__(self):
        return (
            f"{self.lineup.player_registration.player.person.full_name}"
            f" ({self.lineup.match})"
        )