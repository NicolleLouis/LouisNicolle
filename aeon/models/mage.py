from django.db import models
from django.contrib import admin
from django.db.models import UniqueConstraint


class Mage(models.Model):
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

    class Meta:
        constraints = [
            UniqueConstraint(fields=['french_name'], name='unique_mage_french_name'),
            UniqueConstraint(fields=['english_name'], name='unique_mage_english_name')
        ]

    def __str__(self):
        if self.french_name is not None:
            return self.french_name
        if self.english_name is not None:
            return self.english_name
        return str(self.id)


class MageAdmin(admin.ModelAdmin):
    list_display = (
        "french_name",
    )

    search_fields = [
        'french_name',
        'english_name',
    ]
