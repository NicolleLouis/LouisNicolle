from rest_framework import serializers

from aeon.models.mage import Mage


class MageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = [
            "name",
        ]

