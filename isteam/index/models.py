from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

from groupware.models import User


class Session(models.Model):
    title = models.CharField(max_length=30)

    description = models.TextField


class Activity(models.Model):
    start_date = models.DateField

    end_date = models.DateField

    title = models.CharField(max_length=30)

    sessions = models.ForeignKey(Session, on_delete=models.PROTECT)