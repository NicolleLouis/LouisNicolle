from django.utils import timezone
from django.db import models
from django.contrib import admin

from boulder_stats.enums.colors import Colors


class ColorDayEntry(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    number_of_wall_climbed = models.IntegerField(
        blank=True,
        null=True
    )
    grade = models.CharField(
        max_length=12,
        choices=Colors.choices(),
    )
    day = models.DateField(
        default=timezone.now
    )

    @classmethod
    def get_all_attributes(cls):
        all_fields = cls._meta.fields
        return [(field.name, field.name) for field in all_fields]


class ColorDayEntryAdmin(admin.ModelAdmin):
    list_display = (
        'grade',
        "number_of_wall_climbed",
        "day",
    )
