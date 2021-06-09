from django.dispatch import receiver
from django.db.models.signals import pre_save

from aeon.models.spell import Spell


@receiver(pre_save, sender=Spell)
def complete_maximum_damage(sender, instance, **kwargs):
    if instance.maximum_damage is None and instance.damage is not None:
        instance.maximum_damage = instance.damage
