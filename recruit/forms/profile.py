from django import forms


class ProfileForm(forms.Form):
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
