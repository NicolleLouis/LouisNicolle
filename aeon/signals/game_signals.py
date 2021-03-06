from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from aeon.achievements.mage_death_and_victory import MageDeathAndVictory
from aeon.models.game import Game
from aeon.services.card_service import CardService
from aeon.services.game_service import GameService
from aeon.services.mage_service import MageService
from aeon.services.nemesis_service import NemesisService
from stats.service.profile_service import ProfileService


@receiver(post_save, sender=Game)
def compute_data_nemesis(sender, instance, created, **kwargs):
    NemesisService.compute_nemesis_data(instance.nemesis)


@receiver(m2m_changed, sender=Game.mage.through)
def compute_mage_number(sender, instance, **kwargs):
    GameService.update_mage_number(instance)


@receiver(m2m_changed, sender=Game.mage.through)
def compute_data_mage(sender, instance, **kwargs):
    mages = instance.mage.all()
    for mage in mages:
        MageService.compute_mage_data(mage)


@receiver(m2m_changed, sender=Game.cards_in_market.through)
def compute_data_card(sender, instance, **kwargs):
    cards = instance.cards_in_market.all()
    for card in cards:
        CardService.compute_card_data(card)


@receiver(m2m_changed, sender=Game.cards_in_market.through)
def compute_game_info_on_card(sender, instance, **kwargs):
    GameService.update_game_card_info(instance)


@receiver(post_save, sender=Game)
def compute_game_info(sender, instance, **kwargs):
    GameService.update_nemesis_hit_point(instance)


@receiver(m2m_changed, sender=Game.players.through)
def compute_profile_data(sender, instance, **kwargs):
    for profile in instance.players.all():
        ProfileService.update_profile_data(profile)
        MageDeathAndVictory().check_achievement(profile)
