from django.urls import path

from groupware.views.accounts import AccountBookListView
from groupware.views.activities import ActivityListView
from groupware.views.users import UserListView
from django.contrib.auth.decorators import permission_required


urlpatterns = [
    path(
        'activities/',
        permission_required(['groupware.view_activity', 'groupware.view_session'], login_url='signin')(ActivityListView.as_view()),
        name='groupware_activities'
    ),
    path(
        'accounts/',
        permission_required('groupware.view_accountbook', login_url='signin')(AccountBookListView.as_view()),
        name='groupware_accounts'
    ),
    path(
        'users/',
        permission_required('user.view_member', login_url='signin')(UserListView.as_view()),
        name='groupware_users'
    )
]