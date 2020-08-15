from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponse

from .models import User
from .forms import SignUpForm


class SignUp(FormView):
    model = User

    fields = ['student_id', 'email', 'password', 'is_active']

    form_class = SignUpForm    

    template_name = 'signup.html'

    success_url = '/'

    def form_valid(self, form):
        # 해당 메소드는 POST 요청일 때만 실행됨
        valid = form.is_valid()

        if form.is_valid():
            print('Good')
            return super().form_valid(form)
        else:
            return super().form_invalid(form)