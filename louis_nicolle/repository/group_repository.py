class GroupRepository:
    aeon_admin_group_name = "aeon_admin"
    admin_group_name = {
        "aeon": aeon_admin_group_name
    }

    def is_admin(self, user, application_name):
        if application_name not in self.aeon_admin_group_name:
            raise(SystemError("Application name and Group Permission issue"))
        group_name = self.admin_group_name[application_name]
        return user.groups.filter(name=group_name).exists()
