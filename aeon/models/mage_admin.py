from django.contrib import admin

from aeon.services.mage_service import MageService


@admin.action(description='Compute Mage data')
def compute_data(modeladmin, request, queryset):
    for mage in queryset:
        MageService.compute_mage_data(mage)


class MageAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
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
        compute_data,
    )

    @staticmethod
    @admin.display(description='name')
    def get_name(instance):
        return str(instance)
