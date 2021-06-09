from django.contrib import admin

from stats.models.profile import Profile, ProfileAdmin

admin.site.register(Profile, ProfileAdmin)
