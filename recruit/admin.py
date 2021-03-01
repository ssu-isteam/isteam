from django.contrib import admin
from django.db.models import QuerySet

from recruit.models import Answer, Question, Recruitment, Applicant


def make_published(modeladmin, request, queryset: QuerySet):
    published_recruitments = list(Recruitment.objects.filter(is_published=True))

    for recruitment in published_recruitments:
        recruitment.is_published = False

    Recruitment.objects.bulk_update(published_recruitments, fields=['is_published'])
    queryset.update(is_published=True)


make_published.short_description = '모집 공개하기'


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'is_published')

    actions = [make_published]


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(Applicant)