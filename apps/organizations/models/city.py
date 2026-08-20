from django.db import models

from apps.core.base_models import ActiveModel
from apps.organizations.models.country import Country

class City(ActiveModel):
    """
    Represents a city belonging to a country.
    """
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name="cities",)
    name = models.CharField(max_length=100,)

    class Meta:
        ordering = ["country__name","name",]

        constraints = [models.UniqueConstraint(
                fields=["country","name",],
                name="unique_city_per_country",
            )]

    def __str__(self):
        return f"{self.name}, {self.country.name}"

