from django.db import models


class VictoryType(models.TextChoices):
    UNKNOWN = "UNKNOWN", "Unknown"
    NEMESIS_KILL = "NEMESIS_KILL", "Nemesis is killed"
    NEMESIS_DECK_EMPTY = "NEMESIS_DECK_EMPTY", "Nemesis deck is empty"
