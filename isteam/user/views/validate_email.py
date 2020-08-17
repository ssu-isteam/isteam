from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


from user.models import Member
from user.tokens import account_activation_token


def validate_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Member, pk=uid)

        if account_activation_token.check_token(user, token):
            # TODO: 추후 member.user_permissions에 프로젝트 CRUD 할 수 있는 권한, 장부 볼 수 있는 권한 추가
            user.email_verified = True
            user.save()
        return redirect('index')

    except(TypeError, ValueError, OverflowError):
        return redirect('index')