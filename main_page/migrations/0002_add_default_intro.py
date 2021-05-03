# Generated manually 3.1.7 on 2021-04-28

from django.db import migrations


def forwards_func(apps, schema_editor):
    Introduction = apps.get_model("main_page", "Introduction")
    db_alias = schema_editor.connection.alias
    Introduction.objects.using(db_alias).bulk_create([
        Introduction(title="숭실대학교 공식 소모임",
                     body="숭실대학교 공식 소프트웨어학부 소속 소모임으로써 강의실 지원을 받습니다.",
                     photo="intro/ssu.png", activation=1),
        Introduction(title="Naver D2 Campus",
                     body="Naver D2 Campus에서 서버, 행사 등 여러가지 지원을 받는 Partner 동아리로 선정되었습니다.",
                     photo="intro/d2.png", activation=1),
    ])


def reverse_func(apps, schema_editor):
    Introduction = apps.get_model("main_page", "Introduction")
    db_alias = schema_editor.connection.alias
    Introduction.objects.using(db_alias).filter(
        title="숭실대학교 공식 소모임",
        body="숭실대학교 공식 소프트웨어학부 소속 소모임으로써 강의실 지원을 받습니다.",
        photo="intro/ssu.png", activation=1
    ).delete()
    Introduction.objects.using(db_alias).filter(
        title="Naver D2 Campus",
        body="Naver D2 Campus에서 서버, 행사 등 여러가지 지원을 받는 Partner 동아리로 선정되었습니다.",
        photo="intro/d2.png", activation=1
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
