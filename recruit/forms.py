from django import forms

from recruit.models import GroupMember


class RecruitForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=20,
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
        max_length=30,
        label='이메일'
    )

    phone_number = forms.CharField(
        error_messages={
            'required': '전화번호를 입력주세요.'
        },
        max_length=11,
        label='전화번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        student_id = cleaned_data.get('student_id')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        group_member = GroupMember(
            username=username,
            student_id=student_id,
            email=email,
            phone_number=phone_number,
        )

        group_member.save()
