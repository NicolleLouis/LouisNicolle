class ClimaxIngestionService:
    @staticmethod
    def sum_climax(climax_ingestion):
        climax_ingestion = map(
            lambda ingestion: ingestion.climax_amount,
            climax_ingestion
        )
        return sum(climax_ingestion)
