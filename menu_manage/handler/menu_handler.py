from django.views.decorators.http import require_POST

import menu_manage.service.menu_service as menu

"""
操作类型接口统一入口
"""


# 查询菜单列表数据
def get_menu_list(request):
    return menu.get_menu_list()


# 新增菜单列表或者修改
@require_POST
def add_or_edit_menu(request):
    return menu.add_or_edit_menu(request)


# 删除菜单类型
@require_POST
def delete_menu(request):
    return menu.delete_menu(request)
