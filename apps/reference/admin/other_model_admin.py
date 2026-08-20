from django.contrib import admin
from apps.reference.models import EventCategory, EventType, EventOutcome, BodyPart

admin.site.register(EventCategory)
admin.site.register(EventType)
admin.site.register(EventOutcome)
admin.site.register(BodyPart)