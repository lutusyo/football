from django.db import models
from apps.core.base_models import ActiveModel

from apps.reference.models.event_type import EventType
from apps.reference.models.event_category import EventCategory
from apps.reference.models.event_outcome import EventOutcome
from apps.reference.models.body_part  import BodyPart
from apps.reference.models.event_source import EventSource

from .match import Match
from .match_appearance import MatchAppearance
from apps.core.choices import MatchPeriodChoices, EventSourceChoices


class MatchEvent(ActiveModel):
    appearance = models.ForeignKey(MatchAppearance, on_delete=models.PROTECT, related_name="events")
    event_type = models.ForeignKey(EventType, on_delete=models.PROTECT, related_name="events")
    outcome = models.ForeignKey(EventOutcome, on_delete=models.PROTECT, blank=True, null=True, related_name="events")
    body_part = models.ForeignKey(BodyPart, on_delete=models.PROTECT, blank=True, null=True, related_name="events")

    source = models.ForeignKey(EventSource, on_delete=models.PROTECT, related_name="events", null=True, blank=True,)

    period = models.CharField(max_length=4, choices=MatchPeriodChoices.choices)
    second = models.PositiveIntegerField()

    x_start = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    y_start = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    x_end = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    y_end = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)


    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["second"]

    
    @property
    def match(self):
        return self.appearance.lineup.match

    def __str__(self):
        return f"{self.event_type} - {self.appearance}"