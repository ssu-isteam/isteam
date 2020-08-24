from django.contrib import admin

from groupware.models import AccountBook, Activity, Session


admin.site.register(AccountBook)
admin.site.register(Activity)
admin.site.register(Session)