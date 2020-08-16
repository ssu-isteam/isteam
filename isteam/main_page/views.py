from django.shortcuts import render
from django.views.generic import ListView

from groupware.models import Activity, Session


class Index(ListView):
    model = Activity

    context_object_name = 'activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = list(context[self.context_object_name])[:3]

        for activity in context[self.context_object_name]:
            sessions = list(Session.objects.filter(activity=activity.id))
            activity.sessions.extend(sessions)

        return context