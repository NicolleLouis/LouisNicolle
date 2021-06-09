from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import validate_email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def __str__(self):
        if self.first_name is not None or self.last_name is not None:
            first_name = str(self.first_name) if self.first_name is not None else ""
            last_name = str(self.last_name) if self.last_name is not None else ""
            return "{} {}".format(first_name, last_name)
        username = self.user.username
        return username


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
    )

    @staticmethod
    def get_name(instance):
        return str(instance)
