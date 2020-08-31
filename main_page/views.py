from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse

from groupware.models import Activity, Session


class Index(ListView):
    model = Activity

    context_object_name = 'activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = list(context[self.context_object_name])[:3]

        try:
            context['recruit_url'] = reverse('recruit')
            context['recruit_available'] = True
        except:
            context['recruit_available'] = False

        for activity in context[self.context_object_name]:
            sessions = list(Session.objects.filter(activity=activity.id))
            activity.sessions = sessions

        return context