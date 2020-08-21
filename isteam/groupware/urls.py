from django.urls import path

from groupware.views.accounts import AccountBookListView


urlpatterns = [
    path('accounts/', AccountBookListView.as_view(), name='groupware_accounts')
]