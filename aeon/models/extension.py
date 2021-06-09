from django.db import models
from django.contrib import admin


class Extension(models.Model):
    id = models.AutoField(primary_key=True)
    french_name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    english_name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )

    def __str__(self):
        if self.french_name is not None:
            return self.french_name
        if self.english_name is not None:
            return self.english_name
        return str(self.id)


class ExtensionAdmin(admin.ModelAdmin):
    list_display = (
        "french_name",
    )

    search_fields = [
        'french_name',
        'english_name',
    ]
