from climax_tracker.models.climax_profile import ClimaxProfile


class ProfileRepository:
    @staticmethod
    def get_queryset():
        return ClimaxProfile.objects.all()

    @staticmethod
    def get_by_id(profile_id):
        return ClimaxProfile.objects.get(id=profile_id)
