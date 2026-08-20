from django.db import models
from apps.core.base_models import ActiveModel
from .event_category import EventCategory

class EventType(ActiveModel):
    category = models.ForeignKey(EventCategory, on_delete=models.PROTECT, related_name="event_types")
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=30, unique=True)
    display_order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["category__display_order", "display_order", "name"]

    def __str__(self):
        return self.name