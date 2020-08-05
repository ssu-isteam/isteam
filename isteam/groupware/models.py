from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_id = models.CharField(max_length=8)

    name = models.CharField(max_length=10)

    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.student_id} {self.name}<{self.email}>'
