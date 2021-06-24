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
        'nemesis_win_rate_data',
        NemesisWinRateData.as_view(),
        name='nemesis_win_rate_data',
    ),
    path(
        'nemesis_difficulty_win_rate_data',
        NemesisDifficultyWinRateData.as_view(),
        name='nemesis_difficulty_win_rate_data',
    ),
    path(
        'mage_number_win_rate_data',
        MageNumberWinRateData.as_view(),
        name='mage_number_win_rate_data',
    ),
    path(
        'mage_popularity_data',
        MagePopularityData.as_view(),
        name='mage_popularity_data',
    ),
    path(
        'effective_damage_data',
        EffectiveDamageData.as_view(),
        name='effective_damage_data',
    ),
    path(
        'effective_maximum_damage_data',
        EffectiveDamageGraphData.as_view(),
        name='effective_maximum_damage_data',
    ),
    path(
        'average_ether_cost_data',
        AverageEtherCostData.as_view(),
        name='average_ether_cost_data',
    ),
    path(
        'card_characteristic_win_rate_data',
        CardCharacteristicWinRateData.as_view(),
        name='card_characteristic_win_rate_data',
    ),
]
