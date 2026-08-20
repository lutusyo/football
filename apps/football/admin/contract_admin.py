from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = ("player","organization","start_date","end_date","is_professional","is_current",)
    list_filter = ("organization","is_professional","is_current",)
    search_fields = ("player__person__first_name","player__person__last_name",)