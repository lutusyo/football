from django.db import models
from apps.core.base_models import ActiveModel
from apps.matches.models import MatchEvent
from .match_video import MatchVideo

class VideoClip(ActiveModel):
    video = models.ForeignKey(MatchVideo, on_delete=models.CASCADE, related_name="clips")
    event = models.ForeignKey(MatchEvent, on_delete=models.SET_NULL, null=True, blank=True, related_name="video_clips")
    title = models.CharField(max_length=150)
    start_second = models.PositiveIntegerField()
    end_second = models.PositiveIntegerField()
    clip = models.FileField(upload_to="matches/clips/", blank=True, null=True)

    @property
    def duration_seconds(self):
        return max(0, self.end_second - self.start_second)

    def __str__(self):
        return self.title