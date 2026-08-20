from django.db import models
from apps.core.base_models import ActiveModel

class EventCategory(ActiveModel):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    display_order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name