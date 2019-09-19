from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


# 菜单类型表
class MenuManageType(models.Model):
    type_name = models.CharField(max_length=40, null=False, unique=True, help_text='菜单类型名称')
    remark = models.CharField(max_length=120, default=None, null=True, help_text='备注')

    def __str__(self):
        return {
            'id': self.id,
            'type_name': self.type_name,
            'remark': self.remark,
        }


# 菜单表
class MenuManage(models.Model):
    menu_name = models.CharField(max_length=40, null=False, unique=True, help_text='菜单名称')
    menu_type = models.ForeignKey('MenuManageType', on_delete=models.CASCADE)
    menu_path = models.CharField(max_length=40, null=False, unique=True, help_text='菜单路径')
    remark = models.CharField(max_length=120, default=None, null=True, help_text='备注')

    def __str__(self):
        return {
            'id': self.id,
            'menu_name': self.menu_name,
            'menu_type': self.menu_type.__str__(),
            'menu_path': self.menu_path,
            'remark': self.remark,
        }


# 用户菜单权限表
class UserMenuPermission(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, help_text='用户id')
    menu = models.ForeignKey('MenuManage', null=False, on_delete=models.CASCADE, help_text='菜单id')
