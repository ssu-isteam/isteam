import json

import requests
from decouple import config

from django.http import HttpRequest, HttpResponseBadRequest
from django.views.generic import FormView
from django.shortcuts import redirect
from django.urls import reverse

from recruit.forms.profile import ProfileForm
from recruit.models import Recruitment


class ProfileFormView(FormView):
    form_class = ProfileForm

    template_name = 'recruit/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recruitment'] = Recruitment.objects.order_by('year', 'semester').first()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        try:
            res = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                'secret': config('RECAPTCHA_SECRET'),
                'response': form.data['g-recaptcha-response']
            })
            body = res.json()
            success = body['success']
            
            if res.status_code != 200 or not success:
                raise Exception('Captcha failed.')
        except:
            return HttpResponseBadRequest('캡챠 인증에 실패했습니다. 부원 신청을 다시 진행해 주세요.')

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