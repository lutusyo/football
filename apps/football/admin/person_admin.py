from django.contrib import admin

from apps.football.models.person import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "gender",
        "nationality",
        "date_of_birth",
    )

    search_fields = (
        "first_name",
        "middle_name",
        "last_name",
        "preferred_name",
    )

    list_filter = (
        "gender",
        "nationality",
    )