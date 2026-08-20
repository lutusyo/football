from django.contrib import admin
from apps.matches.models.match_appearance import MatchAppearance


@admin.register(MatchAppearance)
class MatchAppearanceAdmin(admin.ModelAdmin):

    list_display = ("lineup","position","minutes_played","rating","is_player_of_match",)
    list_filter = ("position",)
    search_fields = ("lineup__player_registration__player__person__first_name","lineup__player_registration__player__person__last_name",)