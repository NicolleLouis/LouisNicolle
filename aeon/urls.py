from django.urls import path

from aeon.views.effective_damage_view import effective_damage_data_view, render_effective_damage_view
from aeon.views.home import home
from aeon.views.mage_number_win_rate_view import render_mage_number_win_rate_view, mage_number_win_rate_data_view
from aeon.views.mage_popularity_view import render_mage_popularity_view, mage_popularity_data_view
from aeon.views.nemesis_win_rate_view import nemesis_win_rate_data_view, render_nemesis_win_rate_view
from aeon.views.nemesis_difficulty_win_rate_view import render_nemesis_difficulty_win_rate_view, \
    nemesis_difficulty_win_rate_data_view

urlpatterns = [
    path('', home),
    path(
        'nemesis_win_rate',
        render_nemesis_win_rate_view,
        name='nemesis_win_rate_chart'
    ),
    path(
        'nemesis_win_rate_data',
        nemesis_win_rate_data_view,
        name='nemesis_win_rate_data',
    ),
    path(
        'nemesis_difficulty_win_rate',
        render_nemesis_difficulty_win_rate_view,
        name='nemesis_difficulty_win_rate_chart',
    ),
    path(
        'nemesis_difficulty_win_rate_data',
        nemesis_difficulty_win_rate_data_view,
        name='nemesis_difficulty_win_rate_data',
    ),
    path(
        'mage_number_win_rate',
        render_mage_number_win_rate_view,
        name='mage_number_win_rate_chart',
    ),
    path(
        'mage_number_win_rate_data',
        mage_number_win_rate_data_view,
        name='mage_number_win_rate_data',
    ),
    path(
        'mage_popularity',
        render_mage_popularity_view,
        name='mage_popularity_chart',
    ),
    path(
        'mage_popularity_data',
        mage_popularity_data_view,
        name='mage_popularity_data',
    ),
    path(
        'effective_damage',
        render_effective_damage_view,
        name='effective_damage_chart',
    ),
    path(
        'effective_damage_data',
        effective_damage_data_view,
        name='effective_damage_data',
    ),
]
