from django.dispatch import receiver
from django.db.models.signals import post_save

from climax_tracker.models.bet import Bet
from climax_tracker.service.profile_service import ProfileService


@receiver(post_save, sender=Bet)
def compute_profile_bets(sender, instance, created, **kwargs):
    ProfileService.compute_profile_climax_account(instance.winner)
    ProfileService.compute_profile_climax_account(instance.loser)
