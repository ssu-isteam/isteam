from django.db.models import QuerySet

def make_published(modeladmin, request, queryset: QuerySet):
    queryset.update(is_published=True)

make_published.short_description = "모집 공개하기"
