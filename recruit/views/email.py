from django.shortcuts import render


def email_sent(request):
    return render(request, 'recruit/email_sent.html', {
        'address': request.GET.get('address')
    })
