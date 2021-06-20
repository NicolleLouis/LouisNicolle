from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    mail = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        validators=[validate_email],
    )
    birthday = models.DateTimeField(
        null=True,
        blank=True,
    )
    victory_number = models.IntegerField(
        null=True,
        blank=True,
    )
    game_number = models.IntegerField(
        null=True,
        blank=True,
    )

    @property
    def name(self):
        if self.first_name is not None or self.last_name is not None:
            first_name = str(self.first_name) if self.first_name is not None else ""
            last_name = str(self.last_name) if self.last_name is not None else ""
            return "{} {}".format(first_name, last_name)
        username = self.user.username
        return username

    def __str__(self):
        return self.name
