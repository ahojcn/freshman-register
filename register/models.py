from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=48)
    stu_id = models.CharField(max_length=48)
    major = models.CharField(max_length=48)
    qq = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    something = models.CharField(max_length=512)

    def __str__(self):
        return self.name
