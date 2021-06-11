from django.dispatch import receiver
from django.db.models.signals import pre_save

from aeon.models.card import Card


@receiver(pre_save, sender=Card)
def complete_ether_maximum_gain(sender, instance, **kwargs):
    if instance.ether_maximum_gain is None and instance.ether_gain is not None:
        instance.ether_maximum_gain = instance.ether_gain


@receiver(pre_save, sender=Card)
def complete_maximum_damage(sender, instance, **kwargs):
    if instance.maximum_damage is None and instance.damage is not None:
        instance.maximum_damage = instance.damage