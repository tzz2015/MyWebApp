from django.db import models


# Create your models here.


# 菜单类型表
class MenuManageType(models.Model):
    type_name = models.CharField(max_length=40, null=False, unique=True, help_text='菜单类型名称')
    remark = models.CharField(max_length=120, default=None, null=True, help_text='备注')

    def to_dict(self):
        r = {
            'id': self.id,
            'type_name': self.type_name,
            'remark': self.remark,
        }
        return r


# 菜单表
class MenuManage(models.Model):
    menu_name = models.CharField(max_length=40, null=False, unique=True, help_text='菜单名称')
    menu_type = models.ForeignKey('MenuManageType', on_delete=models.CASCADE)
    menu_path = models.CharField(max_length=40, null=False, unique=True, help_text='菜单路径')
    remark = models.CharField(max_length=120, default=None, null=True, help_text='备注')
