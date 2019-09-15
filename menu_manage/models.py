from django.db import models


# Create your models here.


# 菜单类型表
class MenuManageType(models.Model):
    type_name = models.CharField(max_length=20, null=False, unique=True, help_text='菜单名称')
    remark = models.CharField(max_length=120, default=0, null=True, help_text='备注')
