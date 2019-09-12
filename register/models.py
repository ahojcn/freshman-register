from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=48, verbose_name='姓名')
    stu_id = models.CharField(max_length=48, verbose_name='学号')
    major = models.CharField(max_length=48, verbose_name='专业班级')
    qq = models.CharField(max_length=20, verbose_name='qq')
    phone = models.CharField(max_length=30, verbose_name='手机号')
    something = models.CharField(max_length=512, verbose_name='留言')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "新生信息"
        verbose_name_plural = verbose_name
