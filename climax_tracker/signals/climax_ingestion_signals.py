from django.dispatch import receiver
from django.db.models.signals import post_save

from climax_tracker.models.climax_ingestion import ClimaxIngestion
from climax_tracker.service.profile_service import ProfileService


@receiver(post_save, sender=ClimaxIngestion)
def compute_profile_climax_eaten(sender, instance, created, **kwargs):
    ProfileService.compute_climax_eaten(instance.profile)
