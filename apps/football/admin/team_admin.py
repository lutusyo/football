from django.contrib import admin
from apps.football.models.team import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name","organization","category","age_group","is_active",)
    list_filter = ("organization","category","age_group","is_active",)
    search_fields = ("name","organization__name",)
    autocomplete_fields = ("organization",)
