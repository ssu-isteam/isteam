from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import Member
from groupware.models import AccountBook


class GroupwareView(LoginRequiredMixin):
    login_url = '/user/signin/'

    tabs = {
        'activities': '활동',
        'users': '회원명단',
        'accounts': '회계내역'
    }

    tab_items = tabs.items()

    tab_keys = tabs.keys()

    def select_tab(self, selected):
        if selected is not None and selected in self.tabs.keys():
            return selected
        else:
            return list(self.tab_keys)[0]


class AccountBookListView(GroupwareView, ListView):
    model = AccountBook

    template_name = 'account.html'

    context_object_name = 'accounts'

    paginate_by = 2

    tab_name = 'accounts'

    def get_context_data(self):
        context = super().get_context_data()

        context['tabs'] = self.tab_items
        context['selected'] = self.select_tab(self.tab_name)

        return context
