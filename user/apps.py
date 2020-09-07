from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        from django.contrib.auth.models import Group, Permission

        junior_perm_codenames = [
            'view_member',
            'view_accountbook',
            'view_session',
            'view_activity',
            'add_session',
            'change_session',
            'delete_session',
            'view_session'
        ]
        junior_perms = Permission.objects.filter(codename__in=junior_perm_codenames)
        
        senior_perm_codenames = junior_perm_codenames + [
            'add_activity',
            'change_activity',
            'delete_activity'
        ]
        senior_perms = Permission.objects.filter(codename__in=senior_perm_codenames)

        manager_perms = Permission.objects.all()

        junior_group, created = Group.objects.update_or_create(name='junior')
        junior_group.permissions.set(junior_perms)

        senior_group, created = Group.objects.update_or_create(name='senior')
        senior_group.permissions.set(senior_perms)

        manager_group, created = Group.objects.update_or_create(name='manager')
        manager_group.permissions.set(manager_perms)
