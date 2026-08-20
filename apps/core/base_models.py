import uuid
from django.db import models


class BaseModel(models.Model):
    """
    Base model for all business models.
    """

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveModel(BaseModel):
    """
    Adds an active flag to models that can be enabled/disabled.
    """

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True