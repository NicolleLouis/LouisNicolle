from django.db import models
from django.contrib import admin
from django.db.models import UniqueConstraint

from aeon.models.extension import Extension


class Card(models.Model):
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
    ether_cost = models.IntegerField(
        null=True,
        blank=True
    )
    is_self_destroyable = models.BooleanField(
        default=False
    )
    has_utility = models.BooleanField(
        default=False
    )
    extension = models.ForeignKey(
        Extension,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['french_name'], name='unique_card_french_name'),
            UniqueConstraint(fields=['english_name'], name='unique_card_english_name')
        ]

    def name(self):
        name = str(self.id)
        if self.french_name is not None:
            name = self.french_name
        if self.english_name is not None:
            name = self.english_name
        return name

    def __str__(self):
        return self.name()


class CardAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        'ether_cost',
        "is_self_destroyable",
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

    @staticmethod
    @admin.display(description='name')
    def get_name(instance):
        return str(instance)
