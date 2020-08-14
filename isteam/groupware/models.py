from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_id = models.CharField(max_length=8)

    email = models.CharField(max_length=30)

    password = models.CharField(max_length=128)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Student id: {self.student_id}\nName: {self.username}'
