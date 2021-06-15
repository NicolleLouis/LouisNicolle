from django.urls import path

from aeon.views.home import home
from aeon.views.mage_number_win_rate_view import render_mage_number_win_rate_view, mage_number_win_rate_data_view
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
]
