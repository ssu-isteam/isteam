from django.shortcuts import render
from django.views.generic import FormView
from .forms import RecruitForm


class RecruitView(FormView):
    form_class = RecruitForm

    template_name = 'recruit/recruit.html'

    success_url = '/'
