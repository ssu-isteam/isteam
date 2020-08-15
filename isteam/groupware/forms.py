from django import forms
from .models import User
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.Form):
    nickname = forms.CharField(
        error_messages={
            'required': '닉네임을 입력해주세요.'
        },
        max_length=20,
        label='닉네임'
    )

    last_name = forms.CharField(
        error_messages={
            'required': '성을 입력해주세요.'
        },
        max_length=2,
        label='성'
    )

    first_name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=4,
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

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        max_length=128,
        widget=forms.PasswordInput,
        label='비밀번호'
    )

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
        elif User.objects.filter(username=nickname):
            self.add_error('nickname', '이미 존재하는 닉네임입니다.')
        elif User.objects.filter(email=email):
            self.add_error('email', '이미 존재하는 이메일입니다.')
        elif User.objects.filter(student_id=student_id):
            self.add_error('student_id', '이미 존재하는 학번입니다.')
        else:
            user = User(
                username=nickname,
                first_name=cleaned_data.get('first_name'),
                last_name=cleaned_data.get('last_name'),
                student_id=student_id,
                email=email,
                password=make_password(password),
            )
            user.save()
