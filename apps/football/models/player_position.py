from django.db import models

from apps.core.base_models import ActiveModel
from apps.reference.models.position import Position
from .player_profile import PlayerProfile


class PlayerPosition(ActiveModel):
    """
    Links a player to one or more playing positions.
    """

    player = models.ForeignKey(PlayerProfile,on_delete=models.CASCADE,related_name="positions",)
    position = models.ForeignKey(Position,on_delete=models.PROTECT,related_name="players",)
    priority = models.PositiveSmallIntegerField(default=1,help_text="1 = primary position",)
    proficiency = models.PositiveSmallIntegerField(default=100,help_text="Estimated proficiency (0-100).",)

    class Meta:
        ordering = ["priority","position__display_order",]

        constraints = [
            models.UniqueConstraint(
                fields=["player", "position"],
                name="unique_player_position",
            ),
            models.UniqueConstraint(
                fields=["player", "priority"],
                name="unique_player_position_priority",
            ),
        ]

    def __str__(self):
        return (
            f"{self.player.person.full_name} - "
            f"{self.position.short_name}"
        )