from django.db import models


class CardType(models.TextChoices):
    UNKNOWN = "UNKNOWN", "Unknown"
    GEM = "GEM", "Gem"
    RELIC = "RELIC", "Relic"
    SPELL = "SPELL", "Spell"
