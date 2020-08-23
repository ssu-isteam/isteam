from django.views.generic import FormView
from django.contrib.auth import authenticate, login

from user.forms.sign_in import SignInForm


class SignIn(FormView):
    form_class = SignInForm

    template_name = 'sign_in.html'

    success_url = '/groupware/activities'

    def form_valid(self, form):
        nickname = form.data['nickname']
        password = form.data['password']
        member = authenticate(username=nickname, password=password)

        if member is not None and member.email_verified == True:
            login(self.request, member)
            return super().form_valid(form)
        else:
            response = super().form_invalid(form)
            response.status_code = 401
            return response
