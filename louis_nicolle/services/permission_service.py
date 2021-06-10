class PermissionService:
    @staticmethod
    def is_admin(user):
        return user.is_superuser
