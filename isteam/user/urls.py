from django.urls import path

from user.views import sign_up
from user.views import validate_email

urlpatterns = [
    path('signup/', sign_up.SignUp.as_view(), name='signup'),
    path('validate/<str:uidb64>/<str:token>', validate_email.validate_email, name='validate')
]