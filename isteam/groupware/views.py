from django.shortcuts import render
from django.views.generic import DetailView

from user.models import Member


class GroupwareMainPage(DetailView):
    model = Member

    context_object_name = 'member_info'

    template_name = 'index.html'
