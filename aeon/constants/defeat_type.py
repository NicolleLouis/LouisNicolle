from django.db import models


class DefeatType(models.TextChoices):
    UNKNOWN = "UNKNOWN", "Unknown"
    GRAVEHOLD_DEATH = "GRAVEHOLD_DEATH", "Gravehold died"
    MAGE_DEATH = "MAGE_DEATH", "All Mages Died"
    SPECIAL_NEMESIS_DEFEAT = "SPECIAL_NEMESIS_DEFEAT", "Nemesis special win rule"
