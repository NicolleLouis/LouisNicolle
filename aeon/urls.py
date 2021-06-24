from django.urls import path

from aeon.views.average_ether_cost_view import AverageEtherCostData
from aeon.views.card_characteristic_win_rate import CardCharacteristicWinRateData
from aeon.views.effective_damage_view import effective_damage_data_view
from aeon.views.effective_maximum_damage_view import effective_maximum_damage_data_view
from aeon.views.home import home
from aeon.views.mage_number_win_rate_view import mage_number_win_rate_data_view
from aeon.views.mage_popularity_view import mage_popularity_data_view
from aeon.views.nemesis_win_rate_view import nemesis_win_rate_data_view
from aeon.views.nemesis_difficulty_win_rate_view import nemesis_difficulty_win_rate_data_view

urlpatterns = [
    path('', home),
    path(
        'nemesis_win_rate_data',
        nemesis_win_rate_data_view,
        name='nemesis_win_rate_data',
    ),
    path(
        'nemesis_difficulty_win_rate_data',
        nemesis_difficulty_win_rate_data_view,
        name='nemesis_difficulty_win_rate_data',
    ),
    path(
        'mage_number_win_rate_data',
        mage_number_win_rate_data_view,
        name='mage_number_win_rate_data',
    ),
    path(
        'mage_popularity_data',
        mage_popularity_data_view,
        name='mage_popularity_data',
    ),
    path(
        'effective_damage_data',
        effective_damage_data_view,
        name='effective_damage_data',
    ),
    path(
        'effective_maximum_damage_data',
        effective_maximum_damage_data_view,
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
