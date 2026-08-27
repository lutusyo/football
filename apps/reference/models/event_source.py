from django.db import models
from apps.core.base_models import ActiveModel
from apps.core.choices import EventSourceChoices


class EventSource(ActiveModel):

    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    source_type = models.CharField(max_length=20, choices=EventSourceChoices.choices)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name