from climax_tracker.models.climax_profile import ClimaxProfile


class ProfileRepository:
    @staticmethod
    def get_queryset():
        return ClimaxProfile.objects.all()
