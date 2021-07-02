from climax_tracker.repository.bet_repository import BetRepository
from climax_tracker.repository.climax_ingestion_repository import ClimaxIngestionRepository
from climax_tracker.service.bet_service import BetService
from climax_tracker.service.climax_ingestion_service import ClimaxIngestionService


class ProfileService:
    @staticmethod
    def compute_profile_climax_account(profile):
        bets_win = BetRepository.get_bet_win_by_profile(profile)
        total_bet_win = BetService.sum_climax(bets_win)
        profile.total_climax_bet_win = total_bet_win

        bets_lost = BetRepository.get_bet_lost_by_profile(profile)
        total_bet_lost = BetService.sum_climax(bets_lost)
        profile.total_climax_bet_lost = total_bet_lost

        profile.climax_account = min(profile.climax_eaten - total_bet_lost, 0)
        profile.save()

    @staticmethod
    def compute_climax_eaten(profile):
        climax_ingestion = ClimaxIngestionRepository.get_by_profile(profile)
        total_eaten = ClimaxIngestionService.sum_climax(climax_ingestion)
        profile.climax_eaten = total_eaten
        profile.climax_account = min(total_eaten - profile.total_climax_bet_lost, 0)
        profile.save()
