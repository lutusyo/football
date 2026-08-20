from django.contrib import admin

from apps.football.models.player_profile import PlayerProfile


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):

    list_display = ("person","preferred_foot","current_height_cm","current_weight_kg",)
    search_fields = ("person__first_name","person__last_name",)