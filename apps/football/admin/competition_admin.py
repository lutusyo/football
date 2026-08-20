from django.contrib import admin

from apps.football.models.competition import (Competition,CompetitionSeason,TeamCompetitionEntry,)

class CompetitionSeasonInline(admin.TabularInline):
    model = CompetitionSeason
    extra = 0

class TeamCompetitionEntryInline(admin.TabularInline):
    model = TeamCompetitionEntry
    extra = 0
    autocomplete_fields = ("team",)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "country", "competition_type","is_active",)
    list_filter = ("competition_type","country","is_active",)
    search_fields = ("name","short_name","country",)
    inlines = [CompetitionSeasonInline,]

@admin.register(CompetitionSeason)
class CompetitionSeasonAdmin(admin.ModelAdmin):
    list_display = ("competition","season","is_active",)
    list_filter = ("competition","season","is_active",)
    search_fields = ("competition__name","season__name",)
    autocomplete_fields = ("competition","season",)
    ordering = ("-season__start_date","competition__name",)
    inlines = [TeamCompetitionEntryInline,]

@admin.register(TeamCompetitionEntry)
class TeamCompetitionEntryAdmin(admin.ModelAdmin):
    list_display = ("team","competition_season","is_active",)
    list_filter = ("competition_season__competition","competition_season__season","is_active",)
    search_fields = ("team__name","competition_season__competition__name","competition_season__season__name",)
    autocomplete_fields = ("team","competition_season",)
