from stats.models.profile import Profile


class ProfileRepository:
    @staticmethod
    def get_queryset():
        return Profile.objects.all()

    @staticmethod
    def get_by_id(profile_id):
        return Profile.objects.get(user__id=profile_id)
