from django.db import models
from apps.core.base_models import ActiveModel
from apps.core.choices import (PositionLineChoices,PositionSideChoices,)

class Position(ActiveModel):
    """
    Football playing position.
    """
    
    name = models.CharField(max_length=50,unique=True,)
    short_name = models.CharField(max_length=10,unique=True,)

    line = models.CharField(max_length=20,choices=PositionLineChoices.choices,)
    side = models.CharField(max_length=20,choices=PositionSideChoices.choices,blank=True,)

    display_order = models.PositiveSmallIntegerField(default=1,)

    class Meta:
        ordering = [
            "display_order",
            "name",
        ]

    def __str__(self):
        return self.name




