from django.db import migrations


def create_default_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'group')
    Permission = apps.get_model('auth', 'permission')

    codenames = []

    codenames += [
        'view_group',
        'view_member',
        'view_accountbook',
        'view_activity',
        'add_session',
        'change_session',
        'delete_session',
        'view_session',
    ]
    junior_perms = Permission.objects.filter(codename__in=codenames)

    codenames += [
        'add_session',
        'change_session',
        'delete_session',
    ]
    senior_perms = Permission.objects.filter(codename__in=codenames)

    manager_perms = Permission.objects.all()

    Group.objects.using(schema_editor).bulk_create([
        Group(name='junior', permissions=junior_perms),
        Group(name='senior', permissions=senior_perms),
        Group(name='manager', permissions=manager_perms),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
    ]

    operations = [
        migrations.RunPython(create_default_groups)
    ]