from django.db import migrations, models


def forward(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    db_alias = schema_editor.connection.alias

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
    junior_perms = Permission.objects.using(db_alias).filter(codename__in=junior_perm_codenames)
    
    senior_perm_codenames = junior_perm_codenames + [
        'add_activity',
        'change_activity',
        'delete_activity'
    ]
    senior_perms = Permission.objects.using(db_alias).filter(codename__in=senior_perm_codenames)

    manager_perms = Permission.objects.using(db_alias).all()

    junior_group, _ = Group.objects.using(db_alias).update_or_create(name='junior')
    junior_group.permissions.set(junior_perms)
    junior_group.save()

    senior_group, _ = Group.objects.using(db_alias).update_or_create(name='senior')
    senior_group.permissions.set(senior_perms)
    senior_group.save()

    manager_group, _ = Group.objects.using(db_alias).update_or_create(name='manager')
    manager_group.permissions.set(manager_perms)
    manager_group.save()

def backward(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    Group.objects.using(db_alias).all().delete()
    Permission.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('user', '0002_auto_20200828_1637'),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]