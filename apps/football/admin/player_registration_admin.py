from django.contrib import admin
from apps.football.models.player_registration import PlayerRegistration

@admin.register(PlayerRegistration)
class PlayerRegistrationAdmin(admin.ModelAdmin):

    list_display = ("player","team","season","squad_number","status","registration_type","start_date","is_active",)
    list_filter = ("organization","team","season","status","registration_type",)
    search_fields = ("player__person__first_name","player__person__last_name","team__name",)