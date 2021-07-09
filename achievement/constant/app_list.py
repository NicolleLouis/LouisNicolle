from django.db import models


class AppList(models.TextChoices):
    AEON = "AEON", "aeon"
    CLIMAX_TRACKER = "CLIMAX_TRACKER", "climax_tracker"
