from django.urls import path
from django.views.generic import TemplateView

from aeon.views.home import home
from aeon.views.nemesis_win_rate_view import NemesisWinRateView

urlpatterns = [
    path('', home),
    path(
        'nemesis_win_rate',
        TemplateView.as_view(template_name='aeon/nemesis_win_rate.html'),
        name='line_chart'
    ),
    path('nemesis_win_rate_data', NemesisWinRateView().view, name='nemesis_win_rate_data'),
]
