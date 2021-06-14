from django.contrib import admin

from aeon.services.nemesis_service import NemesisService


class NemesisAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "difficulty",
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

    ordering = (
        "difficulty",
    )

    readonly_fields = (
        "game_number",
        "win_rate",
    )

    actions = (
        "compute_data",
    )

    @staticmethod
    @admin.display(description='name')
    def get_name(instance):
        return str(instance)

    @admin.action(description='Compute Nemesis data', permissions=['change'])
    def compute_data(self, request, queryset):
        for nemesis in queryset:
            NemesisService.compute_nemesis_data(nemesis)
