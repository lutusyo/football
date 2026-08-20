from django.db import models
from apps.core.base_models import ActiveModel
from apps.matches.models.match_appearance import MatchAppearance
from apps.matches.models.match_event import MatchEvent

class MatchEventParticipant(ActiveModel):
    class RoleChoices(models.TextChoices):
        PRIMARY = "PRIMARY", "Primary"
        RECEIVER = "RECEIVER", "Receiver"
        ASSISTER = "ASSISTER", "Assister"
        OPPONENT = "OPPONENT", "Opponent"
        OTHER = "OTHER", "Other"

    event = models.ForeignKey(MatchEvent, on_delete=models.CASCADE, related_name="participants")
    appearance = models.ForeignKey(MatchAppearance, on_delete=models.PROTECT, related_name="event_participations")
    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["event", "appearance", "role"], name="unique_event_participant_role")
        ]