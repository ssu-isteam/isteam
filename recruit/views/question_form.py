import json

from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from recruit.forms.question import QuestionForm
from recruit.models import Recruitment, Question, Applicant, Answer
from utils.email import send_template_email
from utils.recaptcha import validate_captcha


class QuestionFormView(FormView):
    form_class = QuestionForm

    template_name = 'recruit/question.html'

    success_url = '/'

    def get_applicant_profile_from_cookie(self):
        applicant_profile = {}

        raw_data = self.request.COOKIES.get('profile')
        json_data = json.loads(raw_data)

        for key in ('username', 'student_id', 'email', 'phone_number'):
            if type(json_data[key]) is not str:
                raise Exception()
            else:
                applicant_profile[key] = json_data[key]

        return applicant_profile

    def form_valid(self, form):
        bad_request = validate_captcha(form.data['g-recaptcha-response'])
        if bad_request:
            return bad_request

        recruitment = Recruitment.objects.filter(is_published=True).first()

        ids = list(form.cleaned_data.keys())

        questions = Question.objects.filter(id__in=map(int, ids), recruitment=recruitment)
        questions = list(questions)

        applicant_profile = self.get_applicant_profile_from_cookie()

        applicant, created = Applicant.objects.update_or_create(
            student_id=applicant_profile['student_id'],
            defaults={
                'recruitment': recruitment,
                'name': applicant_profile['username'],
                'email': applicant_profile['email'],
                'phone_number': applicant_profile['phone_number'],
                'passed': False
            }
        )

        answers = []
        for q in questions:
            answer, created = Answer.objects.update_or_create(
                question=q,
                applicant=applicant,
                defaults={
                    'answer': str(form.cleaned_data[str(q.pk)])
                }
            )
            answers.append(answer)

        send_template_email(
            title=f'{applicant.name}님, ISTEAM에 지원해 주셔서 감사합니다!',
            template_name='recruit/email_body.html',
            to=applicant.email,
            context={
                'applicant': applicant,
                'answers': answers
            }
        )

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        raw_data = self.request.COOKIES.get('profile')

        if raw_data is None:
            return HttpResponseRedirect(reverse('recruit'))

        return super().get(*args, **kwargs)

    def get_success_url(self):
        profile = self.request.COOKIES.get('profile')
        profile = json.loads(profile)
        return f'{reverse("recruit_email_sent")}?address={profile["email"]}'
