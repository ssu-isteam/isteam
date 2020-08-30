import json

from django.http import HttpRequest
from django.views.generic import FormView
from django.shortcuts import redirect
from django.urls import reverse

from recruit.forms.profile import ProfileForm


class ProfileFormView(FormView):
    form_class = ProfileForm

    template_name = 'recruit/profile.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        
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