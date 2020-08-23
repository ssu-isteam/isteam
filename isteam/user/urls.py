from django.urls import path

from user.views import sign_up
from user.views import sign_in
from user.views import sign_out
from user.views import validate_email

urlpatterns = [
    path('signup/', sign_up.SignUp.as_view(), name='signup'),
    path('signin/', sign_in.SignIn.as_view(), name='signin'),
    path('signout/', sign_out.SignOut, name='signout'),
    path('validate/<str:uidb64>/<str:token>', validate_email.validate_email, name='validate')
]