from django.db import models
from apps.core.base_models import ActiveModel

class Country(ActiveModel):
    """
    Represents a country that can contain organizations.
    """
    name = models.CharField(max_length=100,unique=True,)
    code = models.CharField(max_length=3,unique=True,blank=True,)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

