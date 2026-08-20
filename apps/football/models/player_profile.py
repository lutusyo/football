from django.db import models

from apps.core.base_models import ActiveModel
from apps.core.choices import FootChoices
from .person import Person


class PlayerProfile(ActiveModel):
    """
    Football-specific information about a player.
    """
    person = models.OneToOneField(Person,on_delete=models.CASCADE,related_name="player_profile",)
    preferred_foot = models.CharField(max_length=10,choices=FootChoices.choices,)
    jersey_name = models.CharField(max_length=50,blank=True,)
    current_height_cm = models.PositiveSmallIntegerField(blank=True,null=True,)
    current_weight_kg = models.PositiveSmallIntegerField(blank=True,null=True,)
    fifa_connect_id = models.CharField(max_length=100,blank=True,)
    transfermarkt_id = models.CharField(max_length=100,blank=True,)

    def __str__(self):
        return self.person.full_name