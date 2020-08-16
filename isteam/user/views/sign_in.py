from django.views.generic import FormView
from django.contrib.auth import authenticate

from user.forms.sign_in import SignInForm

class SignIn(FormView):
    form_class = SignInForm

    template_name = 'sign_in.html'

    