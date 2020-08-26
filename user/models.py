from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):

    username = models.CharField(max_length=10, null=True, blank=False, unique=True)

    # 학번
    student_id = models.CharField(max_length=8)

    # @soongsil.ac.kr로 끝나는 이메일
    email = models.CharField(max_length=30, null=True, blank=False)

    password = models.CharField(max_length=128, null=True, blank=False)

    # 이메일 인증 여부
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_id} {self.username}'