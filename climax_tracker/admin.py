from django.contrib import admin

from climax_tracker.models.bet import Bet, BetAdmin
from climax_tracker.models.climax_ingestion import ClimaxIngestion, ClimaxIngestionAdmin
from climax_tracker.models.climax_profile import ClimaxProfile, ClimaxProfileAdmin
from climax_tracker.models.pending_bet import PendingBet, PendingBetAdmin

admin.site.register(Bet, BetAdmin)
admin.site.register(ClimaxProfile, ClimaxProfileAdmin)
admin.site.register(ClimaxIngestion, ClimaxIngestionAdmin)
admin.site.register(PendingBet, PendingBetAdmin)
