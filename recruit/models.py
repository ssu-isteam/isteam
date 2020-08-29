from django.db import models


class GroupMember(models.Model):
    username = models.CharField(max_length=5)

    student_id = models.CharField(max_length=8)

    email = models.CharField(max_length=30, default='')

    phone_number = models.CharField(max_length=11)

    approval = models.BooleanField(default=False)