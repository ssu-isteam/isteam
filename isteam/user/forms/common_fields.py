from django import forms


nickname = forms.CharField(
    error_messages={
        'required': '닉네임을 입력해주세요.'
    },
    max_length=20,
    label='닉네임'
)

password = forms.CharField(
    error_messages={
        'required': '비밀번호를 입력해주세요.'
    },
    max_length=128,
    widget=forms.PasswordInput,
    label='비밀번호'
)