from django.contrib import admin

# Register your models here.

from recruit.models import GroupMember


class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'username')


admin.site.register(GroupMember, GroupMemberAdmin)