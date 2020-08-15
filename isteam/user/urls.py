from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('validate/<str:uidb64>/<str:token>', views.validate_email, name='validate')
]