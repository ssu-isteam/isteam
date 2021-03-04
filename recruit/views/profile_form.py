import json

from django.views.generic import FormView
from django.urls import reverse

from recruit.forms.profile import ProfileForm
from recruit.models import Recruitment
from utils.recaptcha import validate_captcha


class ProfileFormView(FormView):
    form_class = ProfileForm

    template_name = 'recruit/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recruitment'] = Recruitment.objects.order_by('year', 'semester').first()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        bad_request = validate_captcha(form.data['g-recaptcha-response'])
        if bad_request:
            return bad_request

        cookie_profile = json.dumps({
            'username': form.cleaned_data['username'],
            'student_id': form.cleaned_data['student_id'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number']
        })
        response.set_cookie('profile', cookie_profile)

        return response

    def get_success_url(self):
        return reverse('recruit_question')
