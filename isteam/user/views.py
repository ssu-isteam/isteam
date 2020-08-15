from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.http import HttpResponseServerError, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect

from .models import Member
from .forms import SignUpForm
from .utils.email import build_template_email
from .tokens import account_activation_token


class SignUp(FormView):
    form_class = SignUpForm    

    template_name = 'signup.html'

    success_url = '/'

    def create_template_email_context(self, form, member):        
        return {
            'user': member,
            'domain': get_current_site(self.request).domain,
            'uid': urlsafe_base64_encode(force_bytes(member.id)),
            'token': account_activation_token.make_token(member)
        }

    # 이 메소드는 POST 요청일 때만 실행됨 
    def form_valid(self, form):
        member = Member(
            nickname=form.data['nickname'],
            username=form.data['name'],
            student_id=form.data['student_id'],
            email=form.data['email'],
            password=make_password(form.data['password']),
        )
        member.save()

        try:
            email = build_template_email(
                title='계정 활성화 확인 이메일', 
                template_name='email_body/activation.html', 
                context=self.create_template_email_context(form.data, member),
                to=form.data['email']
            )
            email.send()
            return super().form_valid(form)
        except:
            member.delete()
            return HttpResponseServerError("500 내부 서버 오류. 이메일 전송에 실패하였습니다. 회원가입을 다시 진행해 주세요.")


def validate_email():
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('index')
    else:
        return redirect('index')