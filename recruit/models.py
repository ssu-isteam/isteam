from django.db import models

from groupware.models import Semester
from .admin_actions import make_published


class Recruitment(models.Model):
    year = models.IntegerField()

    semester = models.IntegerField(choices=Semester.choices(), default=Semester.FIRST)

    information = models.TextField()

    is_published = models.BooleanField(default=False)

    actions = [make_published]

    def __str__(self):
        return f'{self.year}-{self.semester}'


class Question(models.Model):
    question = models.TextField()

    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recruitment.year}-{self.recruitment.semester} {self.question[:10]}... ({self.pk})'


class Applicant(models.Model):
    name = models.CharField(max_length=5)

    student_id = models.CharField(max_length=8)

    email = models.CharField(max_length=30)

    phone_number = models.CharField(max_length=11)

    passed = models.BooleanField(default=False)

    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.student_id})'


class Answer(models.Model):
    answer = models.TextField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'[{self.applicant.student_id}] {self.question.question[:10]}... ({self.pk})'
