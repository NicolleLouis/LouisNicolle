from louis_nicolle.repository.group_repository import GroupRepository


class PermissionService:
    @staticmethod
    def is_admin(user, application_name):
        if user.is_superuser:
            return True
        return GroupRepository().is_admin(
            user=user,
            application_name=application_name
        )

    @staticmethod
    def is_super_user(user):
        return user.is_superuser
