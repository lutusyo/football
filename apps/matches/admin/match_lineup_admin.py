from django.contrib import admin

from apps.matches.models.match_lineup import MatchLineup


@admin.register(MatchLineup)
class MatchLineupAdmin(admin.ModelAdmin):

    list_display = ("match","player_registration","selection_type","shirt_number","is_captain",)
    list_filter = ("selection_type",)
    search_fields = ("player_registration__player__person__first_name","player_registration__player__person__last_name",)