import json

from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse

from recruit.forms.question import QuestionForm
from recruit.models import Recruitment, Question, Applicant


class QuestionFormView(FormView):
    form_class = QuestionForm

    template_name = 'recruit/question.html'

    success_url = '/'

    applicant_profile = {}

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        try:
            profile = self.request.COOKIES.get('profile')
            profile = json.loads(profile)

            for key in ('username', 'student_id', 'email', 'phone_number'):
                if type(profile[key]) is not str:
                    raise Exception()
                else:
                    self.applicant_profile[key] = profile[key]
            
            return super().get(*args, **kwargs)
        except:
            return HttpResponseRedirect(reverse('recruit'))
