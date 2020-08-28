from django.views.generic import FormView
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseServerError, HttpResponseNotAllowed
from django.utils.encoding import force_bytes
from django.db.models import Q

from user.models import Member
from user.forms.sign_up import SignUpForm
from user.tokens import account_activation_token
from user.utils.email import build_template_email

from recruit.models import GroupMember


class SignUp(FormView):
    form_class = SignUpForm    

    template_name = 'recruit.html'

    success_url = '/user/email/sent'

    def create_template_email_context(self, form, member):        
        return {
            'user': member,
            'domain': get_current_site(self.request).domain,
            'uid': urlsafe_base64_encode(force_bytes(member.id)),
            'token': account_activation_token.make_token(member)
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '회원가입'
        return context 

    # 이 메소드는 POST 요청일 때만 실행됨 
    def form_valid(self, form):
        try:
            applicant = GroupMember.objects.get(student_id=form.data['student_id'])

            if not applicant.approval:
                return HttpResponseNotAllowed("부원 신청 진행중입니다. 관리자에게 문의하여 주십시오.")

            member = Member(
                last_name=applicant.username[:1],
                first_name=applicant.username[1:],
                email=applicant.email,
                student_id=applicant.student_id,
                username=form.data['nickname'],
                password=make_password(form.data['password']),
                did_sign_up=True
            )

            member.save()
        except:
            return HttpResponseNotAllowed("부원으로 등록되어 있지 않습니다. 관리자에게 문의하여 주십시오.")

        try:
            email = build_template_email(
                title='계정 활성화 확인 이메일', 
                template_name='email_body/activation.html', 
                context=self.create_template_email_context(form.data, member),
                to=member.email
            )
            self.success_url += f'?address={member.email}'
            member.save()
            email.send()
            return super().form_valid(form)
        except Exception as e:
            print(e)
            return HttpResponseServerError("500 내부 서버 오류. 이메일 전송에 실패하였습니다. 회원가입을 다시 진행해 주세요.")
