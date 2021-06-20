from django.contrib import admin

from aeon.services.mage_service import MageService


class MageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "game_number",
        "win_rate",
    )

    search_fields = [
        'french_name',
        'english_name',
    ]

    autocomplete_fields = (
        "extension",
    )

    list_filter = (
        "extension",
    )

    readonly_fields = (
        "game_number",
        "win_rate",
    )

    ordering = (
        "win_rate",
    )

    actions = (
        "compute_data",
    )

    @admin.action(description='Compute Mage data', permissions=['change'])
    def compute_data(self, request, queryset):
        for mage in queryset:
            MageService.compute_mage_data(mage)
