from django.db import models
from apps.core.base_models import ActiveModel
from apps.organizations.models import Organization


class Venue(ActiveModel):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="venues",)
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100,blank=True,)
    country = models.CharField(max_length=100,blank=True,)
    capacity = models.PositiveIntegerField(blank=True,null=True,)

    def __str__(self):
        return self.name