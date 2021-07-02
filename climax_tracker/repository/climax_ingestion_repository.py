from climax_tracker.models.climax_ingestion import ClimaxIngestion


class ClimaxIngestionRepository:
    @staticmethod
    def get_queryset():
        return ClimaxIngestion.objects.all()

    @staticmethod
    def get_by_profile(profile):
        queryset = ClimaxIngestionRepository.get_queryset()
        queryset = queryset.filter(profile=profile)
        return queryset
