from django.urls import path, include

from recruit.views.profile_form import ProfileFormView
from recruit.views.question_form import QuestionFormView
from recruit.views.email import email_sent


urlpatterns = [
    path('submit/', ProfileFormView.as_view(), name='recruit'),
    path('questions/submit', QuestionFormView.as_view(), name='recruit_question'),
    path('done', email_sent, name='recruit_email_sent')
]
