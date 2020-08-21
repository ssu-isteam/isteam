from django.urls import path

from .views import AccountBookListView


urlpatterns = [
    path('accounts/', AccountBookListView.as_view(), name='groupware_accounts')
]