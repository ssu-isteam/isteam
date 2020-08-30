from django.views.generic import FormView

from recruit.forms.question import QuestionForm
from recruit.models import Recruitment, Question


class QuestionFormView(FormView):
    form_class = QuestionForm

    template_name = 'recruit/question.html'

    success_url = '/'

    def get_context_data(self, **kwargs):
        pass
