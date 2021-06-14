from django.urls import path
from django.views.generic import TemplateView

from aeon.views import nemesis_difficulty_win_rate_view
from aeon.views.home import home
from aeon.views.nemesis_win_rate_view import nemesis_win_rate_view
from aeon.views.nemesis_difficulty_win_rate_view import nemesis_difficulty_win_rate_view


urlpatterns = [
    path('', home),
    path(
        'nemesis_win_rate',
        TemplateView.as_view(template_name='aeon/nemesis_win_rate.html'),
        name='nemesis_win_rate_chart'
    ),
    path(
        'nemesis_win_rate_data',
        nemesis_win_rate_view,
        name='nemesis_win_rate_data',
    ),
    path(
        'nemesis_difficulty_win_rate',
        TemplateView.as_view(template_name='aeon/nemesis_difficulty_win_rate.html'),
        name='nemesis_difficulty_win_rate_chart',
    ),
    path(
        'nemesis_difficulty_win_rate_data',
        nemesis_difficulty_win_rate_view,
        name='nemesis_difficulty_win_rate_data',
    ),
]
