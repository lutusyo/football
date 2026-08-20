from django.db import models
from apps.core.base_models import ActiveModel
from apps.organizations.models import Organization


class Season(ActiveModel):
    """
    A global football season shared by all organizations.

    Examples:
    - 2025/2026
    - 2026/2027
    """

    name = models.CharField(max_length=100,unique=True,)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False,)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.name