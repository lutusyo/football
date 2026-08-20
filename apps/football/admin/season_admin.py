from django.contrib import admin

from apps.football.models.season import Season

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
    "name",
    "start_date",
    "end_date",
    "is_current",
    "is_active",
    )

    list_filter = ("is_current","is_active",)

    search_fields = ("name",)

    ordering = ("-start_date",)