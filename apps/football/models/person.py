from django.db import models
from apps.core.base_models import ActiveModel
from apps.core.choices import GenderChoices


class Person(ActiveModel):
    """
    Stores a person's identity.
    Football-specific information belongs in profile models.
    """

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True,)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100,blank=True,)
    gender = models.CharField(max_length=1,choices=GenderChoices.choices,)
    date_of_birth = models.DateField()
    nationality = models.ForeignKey("organizations.Country",on_delete=models.PROTECT,related_name="people",)
    photo = models.ImageField(upload_to="people/photos/",blank=True,null=True,)

    class Meta:
        ordering = ["last_name","first_name",]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name