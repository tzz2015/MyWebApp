from MyWebApp.json_utils import result_handler, error_handler
from menu_manage.models import MenuManageType
from MyWebApp.utils import is_empty

"""
菜单操作类型 对应表名称：menu_manage_menuType
"""


# 查询类别列表
def get_menu_type_list():
    return result_handler(MenuManageType.objects.all())


# 新增菜单类型
def add_menu_type(request):
    menu_id = int(request.POST.get('id')) if request.POST.get('id') is not None else 0
    type_name = request.POST.get('type_name')
    if is_empty(type_name):
        return error_handler("请输入菜单类别名称")
    remark = request.POST.get('remark')
    # 根据id判断是否存在该菜单类型
    menu = None
    if menu_id is not None and menu_id > 0:
        menu = MenuManageType.objects.filter(id=menu_id)

    if menu is not None and menu.__len__() > 0:
        if type_name == menu[0].type_name:
            MenuManageType.objects.filter(id=menu_id).update(remark=remark)
        else:
            menu = MenuManageType.objects.filter(type_name=type_name)
            if menu.__len__() > 0:
                return error_handler("菜单类别名称重复了！")
            MenuManageType.objects.update.filter(id=menu_id).update(type_name=type_name, remark=remark)
    else:
        # 判断菜单名是否重复
        menu = MenuManageType.objects.filter(type_name=type_name)
        if menu.__len__() > 0:
            return error_handler("菜单类别名称重复了！")
        MenuManageType.objects.create(type_name=type_name, remark=remark)
    return result_handler(data=None)


# 删除菜单名称
def delete_menu_type(request):
    menu_id = int(request.POST.get('id')) if request.POST.get('id') is not None else 0
    find_menu = MenuManageType.objects.filter(id=menu_id)
    if find_menu is None or find_menu.__len__() == 0:
        return error_handler("菜单类别不存在")
    MenuManageType.objects.filter(id=menu_id).delete()
    return result_handler(data=None)
