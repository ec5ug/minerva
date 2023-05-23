from django.contrib import admin
from oauth_app.models import UserInfo
from minerva.models import Scholarship, Error_Report

admin.site.register(UserInfo)
admin.site.register(Scholarship)
admin.site.register(Error_Report)