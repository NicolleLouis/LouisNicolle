from django.urls import path

from climax_tracker.views.bet import BetView
from climax_tracker.views.florent import FlorentView
from climax_tracker.views.finish_pending_bet import FinishPendingBetView
from climax_tracker.views.pending_bet import PendingBetView
from climax_tracker.views.profile import ProfileView
from climax_tracker.views.profile_detail import ProfileDetailView

urlpatterns = [
    path('bet', BetView.as_view()),
    path('finish_pending_bet', FinishPendingBetView.as_view()),
    path('florent', FlorentView.as_view()),
    path('pending_bet', PendingBetView.as_view()),
    path('profile', ProfileView.as_view()),
    path('profile/<int:profile_id>', ProfileDetailView.as_view()),
]
