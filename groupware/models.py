from enum import IntEnum

from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

from user.models import Member


class Semester(IntEnum):
    FIRST = 1

    SECOND = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Activity(models.Model):
    start_date = models.DateField(null=True, blank=False)

    end_date = models.DateField(null=True, blank=True)

    title = models.CharField(max_length=75)

    cover_photo_url = models.CharField(max_length=100, default='')

    sessions = []

    def __str__(self):
        return f'Title: {self.title}'


class Session(models.Model):
    title = models.CharField(max_length=30)

    description = models.TextField(null=True, blank=False)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)


class AccountBook(models.Model):
    year = models.PositiveIntegerField()

    semester = models.IntegerField(choices=Semester.choices(), default=Semester.FIRST)

    embedded_link = models.CharField(max_length=200)
