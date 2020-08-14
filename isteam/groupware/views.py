from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm


# Create your views here.

class Register(FormView):
    form_class = RegisterForm
    success_url = '/../'
