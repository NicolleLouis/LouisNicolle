from django.db import models
from django.db.models import UniqueConstraint

from aeon.models.extension import Extension


class Nemesis(models.Model):
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
    difficulty = models.IntegerField(
        null=True,
        blank=True
    )
    extension = models.ForeignKey(
        Extension,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    game_number = models.IntegerField(
        null=True,
        blank=True,
    )
    win_rate = models.FloatField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['french_name'], name='unique_nemesis_french_name'),
            UniqueConstraint(fields=['english_name'], name='unique_nemesis_english_name')
        ]

    def __str__(self):
        if self.english_name is not None:
            return self.english_name
        if self.french_name is not None:
            return self.french_name
        return str(self.id)
