from django.views.decorators.http import require_POST

import menu_manage.service.menu_type_service as menu_type

"""
操作类型接口统一入口
"""


# 查询菜单列表数据
def get_menu_type_list(request):
    return menu_type.get_menu_type_list()


# 新增菜单列表或者修改
@require_POST
def create_menu_type(request):
    return menu_type.add_menu_type(request)


# 删除菜单类型
@require_POST
def delete_menu_type(request):
    return menu_type.delete_menu_type(request)
