class BetService:
    @staticmethod
    def sum_climax(bets):
        bets = map(
            lambda bet: bet.climax_amount,
            bets
        )
        return sum(bets)
