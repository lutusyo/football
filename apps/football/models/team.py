from django.db import models
from apps.core.base_models import ActiveModel
from apps.organizations.models import Organization
from apps.football.models.season import Season
from apps.core.choices import TeamCategoryChoices, AgeGroupChoices

class Team(ActiveModel):
    """
    Represents a football team within an organization.
    """
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="teams",)
    name = models.CharField(max_length=100,)
    short_name = models.CharField(max_length=30,blank=True,)
    category = models.CharField(max_length=30,choices=TeamCategoryChoices.choices,)
    age_group = models.CharField(max_length=15,choices=AgeGroupChoices.choices,blank=True,)

    class Meta:
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["category","age_group", "name"],
                name="unique_team_per_category_and_age_group",
            )
        ]

    def __str__(self):
        return f"{self.organization.short_name} - {self.name}"