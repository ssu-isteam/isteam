from django.views.generic import ListView

from groupware.views.base import GroupwareView
from groupware.models import Activity, Session


class ActivityListView(GroupwareView, ListView):
    model = Activity

    template_name = 'groupware/activities.html'

    tab_name = 'activities'

    context_object_name = 'activities'

    paginate_by = 3

    ordering = '-start_date'

    def get_context_data(self):
        context = super().get_context_data()

        context['tabs'] = self.tab_items
        context['selected'] = self.select_tab(self.tab_name)
        context['member_info'] = self.request.user

        for activity in context[self.context_object_name]:
            sessions = list(Session.objects.filter(activity=activity.id))
            activity.sessions = sessions

        return context
