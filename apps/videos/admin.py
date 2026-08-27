from django.contrib import admin

from .models.match_video import MatchVideo
from .models.video_clip import VideoClip

admin.site.register(MatchVideo)
admin.site.register(VideoClip)
