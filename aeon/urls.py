from django.urls import path

from aeon.views.average_ether_cost_view import AverageEtherCostData
from aeon.views.card_characteristic_win_rate import CardCharacteristicWinRateData
from aeon.views.effective_damage_view import EffectiveDamageData
from aeon.views.effective_maximum_damage_view import EffectiveDamageGraphData
from aeon.views.home import home
from aeon.views.mage_number_win_rate_view import MageNumberWinRateData
from aeon.views.mage_popularity_view import MagePopularityData
from aeon.views.nemesis_win_rate_view import NemesisWinRateData
from aeon.views.nemesis_difficulty_win_rate_view import NemesisDifficultyWinRateData

urlpatterns = [
    path('', home),
    path(
        'nemesis_win_rate',
        NemesisWinRateData.as_view(),
        name='nemesis_win_rate',
    ),
    path(
        'nemesis_difficulty_win_rate',
        NemesisDifficultyWinRateData.as_view(),
        name='nemesis_difficulty_win_rate',
    ),
    path(
        'mage_number_win_rate',
        MageNumberWinRateData.as_view(),
        name='mage_number_win_rate',
    ),
    path(
        'mage_popularity',
        MagePopularityData.as_view(),
        name='mage_popularity',
    ),
    path(
        'effective_damage',
        EffectiveDamageData.as_view(),
        name='effective_damage',
    ),
    path(
        'effective_maximum_damage',
        EffectiveDamageGraphData.as_view(),
        name='effective_maximum_damage',
    ),
    path(
        'average_ether_cost',
        AverageEtherCostData.as_view(),
        name='average_ether_cost',
    ),
    path(
        'card_characteristic_win_rate',
        CardCharacteristicWinRateData.as_view(),
        name='card_characteristic_win_rate',
    ),
]
