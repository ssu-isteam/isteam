from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 학번
    student_id = models.CharField(max_length=8)

    # @soongsil.ac.kr로 끝나는 이메일
    email = models.CharField(max_length=30)

    # 비밀번호
    password = models.CharField(max_length=128)

    # 소모임에서 활동하고 있는 멤버인지 여부
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Student id: {self.student_id}\nName: {self.username}'