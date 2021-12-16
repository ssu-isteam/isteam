from django.urls import reverse
from django.views.generic import ListView

from groupware.models import Activity, Session
from recruit.functions import is_recruitment_available
from .models import Introduction


class Index(ListView):
    model = Activity

    context_object_name = 'activities'

    queryset = Activity.objects.order_by('-start_date')

    template_name = 'main_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = list(context[self.context_object_name])[:3]
        context[self.context_object_name].reverse()

        context['recruit_available'] = is_recruitment_available()
        context['recruit_url'] = reverse('recruit')

        for activity in context[self.context_object_name]:
            sessions = list(Session.objects.filter(activity=activity.id))
            activity.sessions = sessions

        context['introductions'] = Introduction.objects.filter(activation=True)

        return context
