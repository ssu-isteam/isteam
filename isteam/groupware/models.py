from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_id = models.CharField(max_length=8)

    name = models.CharField(max_length=10)

    email = models.CharField(max_length=30)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Student id: {self.student_id}\nName: {self.name}'
