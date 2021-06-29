from django.urls import path

from aeon.views.average_ether_cost_view import AverageEtherCostData
from aeon.views.card_characteristic_win_rate import CardCharacteristicWinRateData
from aeon.views.effective_damage_view import EffectiveDamageData
from aeon.views.effective_maximum_damage_view import EffectiveDamageGraphData
from aeon.views.home import home
from aeon.views.mage_list import MageView
from aeon.views.mage_number_win_rate_view import MageNumberWinRateData
from aeon.views.mage_popularity_view import MagePopularityData
from aeon.views.nemesis_win_rate_view import NemesisWinRateData
from aeon.views.nemesis_difficulty_win_rate_view import NemesisDifficultyWinRateData

urlpatterns = [
    path('', home),
    path('average_ether_cost', AverageEtherCostData.as_view()),
    path('card_characteristic_win_rate', CardCharacteristicWinRateData.as_view()),
    path('effective_damage', EffectiveDamageData.as_view()),
    path('effective_maximum_damage', EffectiveDamageGraphData.as_view()),
    path('mage', MageView.as_view()),
    path('mage_number_win_rate', MageNumberWinRateData.as_view()),
    path('mage_popularity', MagePopularityData.as_view()),
    path('nemesis_difficulty_win_rate', NemesisDifficultyWinRateData.as_view()),
    path('nemesis_win_rate', NemesisWinRateData.as_view()),
]
