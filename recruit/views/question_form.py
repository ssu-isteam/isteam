import json

from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from recruit.forms.question import QuestionForm
from recruit.models import Recruitment, Question, Applicant, Answer
from utils.email import send_template_email
from utils.recaptcha import get_captcha_data


class QuestionFormView(FormView):
    form_class = QuestionForm

    template_name = 'recruit/question.html'

    success_url = '/'

    applicant_profile = {}

    def form_valid(self, form):
        try:
            res = get_captcha_data(form.data['g-recaptcha-response'])
            body = res.json()
            success = body['success']
            
            if res.status_code != 200 or not success:
                raise Exception('Captcha failed.')
        except:
            return HttpResponseBadRequest('캡챠 인증에 실패했습니다.')

        recruitment = Recruitment.objects.order_by('year', 'semester').first()

        ids = list(form.cleaned_data.keys())

        questions = Question.objects.filter(id__in=map(int, ids), recruitment=recruitment)
        questions = list(questions)

        applicant_name = self.applicant_profile['username']
        applicant_email = self.applicant_profile['email']

        applicant, created = Applicant.objects.update_or_create(
            student_id=self.applicant_profile['student_id'],
            defaults={
                'recruitment': recruitment,
                'name': self.applicant_profile['username'],
                'email': self.applicant_profile['email'],
                'phone_number': self.applicant_profile['phone_number'],
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

    def get_success_url(self):
        profile = self.request.COOKIES.get('profile')
        profile = json.loads(profile)
        return f'{reverse("recruit_email_sent")}?address={profile["email"]}'
