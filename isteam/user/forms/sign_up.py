from django import forms

from user.models import Member
from user.forms.common_fields import nickname, password


class SignUpForm(forms.Form):
    nickname = nickname

    name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=15,
        label='이름'
    )

    student_id = forms.CharField(
        error_messages={
            'required': '학번을 입력해주세요.'
        },
        max_length=8,
        label='학번'
    )

    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        widget=forms.EmailInput,
        max_length=64,
        label='이메일'
    )

    password = password

    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 다시 입력해주세요.'
        },
        max_length=128,
        widget=forms.PasswordInput,
        label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        nickname = cleaned_data.get('nickname')
        student_id = cleaned_data.get('student_id')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
        elif Member.objects.filter(username=nickname).exists():
            self.add_error('nickname', '이미 존재하는 닉네임입니다.')
        elif Member.objects.filter(email=email).exists():
            self.add_error('email', '이미 존재하는 이메일입니다.')
        elif Member.objects.filter(student_id=student_id).exists():
            self.add_error('student_id', '이미 존재하는 학번입니다.')