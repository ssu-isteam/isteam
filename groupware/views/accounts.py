from django.views.generic import ListView

from groupware.models import AccountBook
from groupware.views.base import GroupwareView


class AccountBookListView(GroupwareView, ListView):
    model = AccountBook

    template_name = 'groupware/account.html'

    context_object_name = 'accounts'

    paginate_by = 2

    tab_name = 'accounts'

    ordering = '-id'

    ordering

    def get_context_data(self):
        context = super().get_context_data()

        context['tabs'] = self.tab_items
        context['selected'] = self.select_tab(self.tab_name)
        context['member_info'] = self.request.user

        return context
