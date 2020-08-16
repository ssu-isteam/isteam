from django.views.generic import FormView
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseServerError
from django.utils.encoding import force_bytes

from user.models import Member
from user.forms import SignUpForm
from user.tokens import account_activation_token
from user.utils.email import build_template_email


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
