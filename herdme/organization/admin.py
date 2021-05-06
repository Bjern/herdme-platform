from django.contrib import admin
from .models import Organization


class OrganizationMembers(admin.TabularInline):
    model = Organization.members.through


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'code']
    list_display = ['name', 'code']
    search_fields = ['name', 'code']
    inlines = [
        OrganizationMembers,
    ]
