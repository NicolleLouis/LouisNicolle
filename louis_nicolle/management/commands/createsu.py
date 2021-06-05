from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="louis").exists():
            # Replace create_user by create_super_user if needed
            User.objects.create_superuser("louis", "louisxnicolle@gmail.com", "changeme")
