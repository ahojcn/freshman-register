from django.contrib import admin
from .models import UserInfo


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'major', 'qq', 'phone']
    list_filter = ['name', 'major', 'qq', 'phone', 'stu_id']
    search_fields = ['name', 'major', 'qq', 'phone', 'stu_id']
    list_per_page = 10


admin.site.register(UserInfo, UserInfoAdmin)
