from django.contrib import admin

from apps.football.models import PlayerPosition


@admin.register(PlayerPosition)
class PlayerPositionAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "position",
        "priority",
        "proficiency",
    )

    list_filter = (
        "position",
    )

    search_fields = (
        "player__person__first_name",
        "player__person__last_name",
        "position__name",
    )