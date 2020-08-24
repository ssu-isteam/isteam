from django.contrib.auth import logout
from django.shortcuts import redirect


def SignOut(request):
    logout(request)
    return redirect('index')
