from django.db import models

from groupware.models import Semester


class Recruitment(models.Model):
    year = models.IntegerField()

    semester = models.IntegerField(choices=Semester.choices(), default=Semester.FIRST)


class Question(models.Model):
    question = models.TextField()

    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)


class Applicant(models.Model):
    name = models.CharField(max_length=5)

    student_id = models.CharField(max_length=8)

    email = models.CharField(max_length=30)

    phone_number = models.CharField(max_length=11)

    passed = models.BooleanField(default=False)

    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.TextField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, default=1)
