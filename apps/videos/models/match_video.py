from django.db import models
from apps.core.base_models import ActiveModel
from apps.matches.models import Match

class MatchVideo(ActiveModel):
    class SourceChoices(models.TextChoices):
        UPLOAD = "UPLOAD", "Upload"
        EXTERNAL = "EXTERNAL", "External"

    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=150)
    video = models.FileField(upload_to="matches/videos/", blank=True, null=True)
    external_url = models.URLField(blank=True)
    source = models.CharField(max_length=20, choices=SourceChoices.choices, default=SourceChoices.UPLOAD)
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.match} - {self.title}"