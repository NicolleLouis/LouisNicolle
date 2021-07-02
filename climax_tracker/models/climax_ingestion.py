from django.db import models
from django.contrib import admin

from climax_tracker.models.climax_profile import ClimaxProfile


class ClimaxIngestion(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(
        ClimaxProfile,
        on_delete=models.CASCADE,
        related_name="eater",
    )
    climax_amount = models.IntegerField(
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "{}: {} climax".format(self.profile, self.climax_amount)


class ClimaxIngestionAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'climax_amount',
    )

