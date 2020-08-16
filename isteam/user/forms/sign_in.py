from django.forms import Form

from user.forms.common_fields import nickname, password


class SignInForm(Form):
    nickname = nickname

    password = password
