from django.db import models
from apps.core.base_models import ActiveModel

class BodyPart(ActiveModel):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name