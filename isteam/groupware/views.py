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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        tabs = {
            'activities': '활동',
            'users': '회원명단',
            'account': '회계내역'
        }
        selected = self.request.GET.get('tab')

        if selected is not None and selected in tabs.keys():
            context['selected'] = selected
        else:
            context['selected'] = list(tabs.keys())[0]
        
        context['tabs'] = tabs.items()

        return context
