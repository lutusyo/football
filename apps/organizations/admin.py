from django.contrib import admin

from apps.organizations.models import (City,Country,Organization,)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ( "name","code","is_active",)
    search_fields = ("name","code",)
    list_filter = ("is_active",)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name","country","is_active",)
    search_fields = ("name","country__name",)
    list_filter = ("country","is_active",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
    "name",
    "short_name",
    "country",
    "city",
    "is_active",
    )

    search_fields = (
        "name",
        "short_name",
    )

    list_filter = (
        "country",
        "is_active",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
