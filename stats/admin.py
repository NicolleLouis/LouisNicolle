from django.contrib import admin

from stats.models.profile import Profile
from stats.models.profile_admin import ProfileAdmin

admin.site.register(Profile, ProfileAdmin)
