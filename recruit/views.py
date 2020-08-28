from django.shortcuts import render
from django.views.generic import FormView
from .forms import RecruitForm

# Create your views here.


class RecruitView(FormView):
    form_class = RecruitForm
    template_name = 'recruit.html'
    success_url = '/'
