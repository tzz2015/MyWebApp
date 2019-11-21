# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    """
    用户信息
    """
    id = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    user_type = models.IntegerField(default=0, null=False, help_text='用户角色 0：超级管理员，1：管理员 2：普通用户')


class AlumModel(models.Model):
    """
    相册信息
    """
    key = models.CharField(max_length=255, primary_key=True, help_text='唯一id')
    user = models.ForeignKey('UserInfo', null=False, on_delete=models.CASCADE, help_text='用户id')
    bg_url = models.CharField(max_length=255, null=False, help_text='背景图片地址')
    music_url = models.CharField(max_length=255, null=True, help_text='音乐地址')
    image_urls = models.TextField(null=False, help_text='图片链接，用逗号分隔')
    email = models.EmailField(null=True, help_text='通知邮箱')
    createTime = models.DateTimeField(auto_now=True, help_text='时间')


class PayModel(models.Model):
    """
    支付状态
    """
    alum = models.ForeignKey('AlumModel', null=False, on_delete=models.CASCADE, help_text='用户id')
    user = models.ForeignKey('UserInfo', null=False, on_delete=models.CASCADE, help_text='用户id')
    pay_status = models.IntegerField(default=0, help_text='支付状态')
    createTime = models.DateTimeField(auto_now=True, help_text='时间')
