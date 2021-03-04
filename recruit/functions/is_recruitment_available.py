from recruit.models import Recruitment


def is_recruitment_available() -> bool:
    return Recruitment.objects.filter(is_published=True).exists()
