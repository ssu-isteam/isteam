from django.urls import path

from user.views import sign_up
from user.views import sign_in
from user.views import sign_out
from user.views.email import email_sent, email_verified, verify_email

urlpatterns = [
    path('signup/', sign_up.SignUp.as_view(), name='signup'),
    path('signin/', sign_in.SignIn.as_view(), name='signin'),
    path('signout/', sign_out.SignOut, name='signout'),
    path('email/sent/', email_sent, name='email_sent'),
    path('email/verified/', email_verified, name='email_verified'),
    path('email/verify/<str:uidb64>/<str:token>', verify_email, name='validate')
]