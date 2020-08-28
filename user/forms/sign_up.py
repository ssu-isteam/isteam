from django import forms
from django.db.models import Q

from user.models import Member
from user.forms.common_fields import nickname, password, student_id


class SignUpForm(forms.Form):
    nickname = nickname

    student_id = student_id

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

        re_password_is_same = cleaned_data.get('password') != cleaned_data.get('re_password')

        if re_password_is_same:
            self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
            return

        isteam_member = Member.objects.filter(Q(student_id=cleaned_data.get('student_id'))).exists()

        if not isteam_member:
            self.add_error('student_id', 'ISTEAM 부원이 아닙니다.')
            return
