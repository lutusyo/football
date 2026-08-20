from django.db import models
from apps.core.base_models import BaseModel
from apps.organizations.models.country import Country
from apps.organizations.models.city import City

class Organization(BaseModel):
    """
    Represents a football club using the platform.
    """
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="organizations")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name="organizations", blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True,null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="organizations/logos/",blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name

