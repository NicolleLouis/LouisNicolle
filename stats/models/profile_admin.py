from django.contrib import admin

from achievement.service.achievement_service import AchievementService
from louis_nicolle.services.permission_service import PermissionService
from stats.service.profile_service import ProfileService


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "victory_number",
        "game_number",
        "achievements",
    )

    readonly_fields = (
        "victory_number",
        "game_number"
    )

    search_fields = (
        "first_name",
        'last_name',
        'user__username',
        'name',
    )

    actions = (
        "compute_data",
        "check_all_achievements",
    )

    def get_queryset(self, request):
        queryset = super(ProfileAdmin, self).get_queryset(request)
        if PermissionService.is_super_user(request.user):
            return queryset
        return queryset.filter(user=request.user)

    @admin.action(description='Compute Profile data', permissions=['change'])
    def compute_data(self, request, queryset):
        for profile in queryset:
            ProfileService.update_profile_data(profile)

    @admin.action(description='Check all achievement', permissions=['change'])
    def check_all_achievements(self, request, queryset):
        achievements = AchievementService.get_all_achievements()
        for profile in queryset:
            for achievement in achievements:
                achievement.check_achievement(profile)
