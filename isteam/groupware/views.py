from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import Member


class GroupwareMainPage(LoginRequiredMixin, DetailView):
    login_url = '/user/signin/'

    model = Member

    context_object_name = 'member_info'

    template_name = 'groupware.html'

    def get_object(self):
        return self.request.user
