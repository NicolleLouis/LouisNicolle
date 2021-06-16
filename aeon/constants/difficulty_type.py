from django.db import models


class DifficultyType(models.TextChoices):
    STANDARD = "STANDARD", "Standard"
    HARD = "HARD", "Hard"
