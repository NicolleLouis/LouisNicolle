from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from aeon.models.game import Game
from aeon.services.mage_service import MageService
from aeon.services.nemesis_service import NemesisService


@receiver(post_save, sender=Game)
def compute_data_nemesis(sender, instance, created, **kwargs):
    NemesisService.compute_nemesis_data(instance.nemesis)


@receiver(m2m_changed, sender=Game.mage.through)
def compute_data_mage(sender, instance, **kwargs):
    mages = instance.mage.all()
    for mage in mages:
        MageService.compute_mage_data(mage)
