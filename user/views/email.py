from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import Group

from user.models import Member
from user.tokens import account_activation_token


def email_sent(request):
    return render(request, 'user/email_sent.html', {
        'address': request.GET.get('address')
    })


def email_verified(request):
    return render(request, 'user/email_verified.html', {})


def verify_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Member, pk=uid)

        if account_activation_token.check_token(user, token):
            # junior_group = Group.objects.get(pk=1)
            # user.groups.add(junior_group)

            user.is_active = True
            user.save()
        return redirect('email_verified')

    except(TypeError, ValueError, OverflowError):
        return redirect('index')
