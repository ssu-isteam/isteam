from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import Member
from groupware.views.base import GroupwareView


class UserListView(GroupwareView, ListView):
    model = Member

    template_name = 'users.html'

    context_object_name = 'Users'

    tab_name = 'users'

    def get_queryset(self):
        new_context = Member.objects.filter(is_active=True).order_by('student_id')
        return new_context

    def get_context_data(self):
        context = super().get_context_data()

        context['tabs'] = self.tab_items
        context['selected'] = self.select_tab(self.tab_name)
        context['member_info'] = self.request.user

        return context
