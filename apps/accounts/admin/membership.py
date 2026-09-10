from django.contrib import admin
from ..models import Membership

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "is_active")
    list_filter = ("role", "organization", "is_active")
    search_fields = ("user__username", "user__email", "organization__name")