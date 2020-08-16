from django.views.generic import FormView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from user.forms.sign_in import SignInForm

class SignIn(FormView):
    form_class = SignInForm

    template_name = 'sign_in.html'

    success_url = '/'

    def form_valid(self, form):
        nickname = form.data['nickname']
        password = check_password(form.data['password'])
        member = authenticate(username='ddd', password=password)

        if member is not None:
            self.request.session.set_test_cookie()
            self.request.session['hello'] = 'world'
            self.request.session.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
