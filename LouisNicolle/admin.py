from django.contrib import admin
from django.contrib import auth
import django.contrib.auth.models

from boulder_stats.models.color_day_entry import ColorDayEntry, ColorDayEntryAdmin

# Register your models here.
admin.site.register(ColorDayEntry, ColorDayEntryAdmin)

admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)
