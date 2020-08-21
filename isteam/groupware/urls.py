from django.urls import path

from groupware.views.accounts import AccountBookListView
from groupware.views.users import UserListView


urlpatterns = [
    path('accounts/', AccountBookListView.as_view(), name='groupware_accounts'),
    path('users/', UserListView.as_view(), name='groupware_users'),
]