from django.contrib import admin
from apps.reference.models.position import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name","short_name","line","side","display_order","is_active",)
    list_filter = ("line","side","is_active",)
    search_fields = ("name","short_name",)
    ordering = ("display_order","name",)
    list_editable = ("display_order","is_active",)