from django.dispatch import receiver
from django.db.models.signals import pre_save

from aeon.models.gem import Gem


@receiver(pre_save, sender=Gem)
def complete_ether_maximum_gain(sender, instance, **kwargs):
    if instance.ether_maximum_gain is None and instance.ether_gain is not None:
        instance.ether_maximum_gain = instance.ether_gain
