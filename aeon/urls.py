from django.urls import path

from aeon.views.home import home
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
]
