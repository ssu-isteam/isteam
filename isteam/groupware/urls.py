from django.urls import path

from groupware.views.accounts import AccountBookListView
from groupware.views.activities import ActivityListView


urlpatterns = [
    path('activities/', ActivityListView.as_view(), name='groupware_activities'),
    path('accounts/', AccountBookListView.as_view(), name='groupware_accounts')
]