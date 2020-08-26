from django.contrib import admin

from user.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'username')


admin.site.register(Member, MemberAdmin)
