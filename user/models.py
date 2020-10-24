from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):

    # 학번
    student_id = models.CharField(max_length=8)

    email = models.CharField(max_length=30, default='')

    password = models.CharField(max_length=128, null=True, blank=False)

    is_regular_member = models.BooleanField(default=False)

    # 회원가입 여부
    did_sign_up = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_id} {self.last_name}{self.first_name}'
