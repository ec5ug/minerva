from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from oauth_app.models import UserInfo

# Register your models here.
# class UserInfoInline(admin.StackedInline):
#     model = UserInfo
#     can_delete = False
#     verbose_name_plural = 'UserInfo'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = [UserInfoInline]
#
# admin.site.unregister(User)
# # admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(UserInfo)