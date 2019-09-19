from MyWebApp.json_utils import result_handler, error_handler, format_data
from menu_manage.models import MenuManage, MenuManageType
from MyWebApp.utils import is_empty
from django.forms.models import model_to_dict

"""
菜单操作类型 对应表名称：menu_manage_menu_manage
"""


# 查询类别列表
def get_menu_list():
    menu_list = MenuManage.objects.all().order_by('menu_type_id')
    rest = []
    for menu in menu_list:
        rest.append(menu.__str__())
    print(rest)
    return result_handler(rest)


# 根据菜单类型查询菜单列表
def get_menu_list_by_type():
    menu_type = MenuManageType.objects.all().values()
    for item in menu_type:
        menu_list = MenuManage.objects.filter(menu_type_id=item['id']).all()
        item['child_List'] = format_data(menu_list)
    return result_handler(data=menu_type)


# 新增或者更新菜单类型
def add_or_edit_menu(request):
    menu_id = int(request.POST.get('id')) if not is_empty(request.POST.get('id')) else 0
    menu_name = request.POST.get('menu_name')
    menu_path = request.POST.get('menu_path')
    menu_type_id = int(request.POST.get('menu_type_id')) if not is_empty(request.POST.get('menu_type_id')) else 0
    remark = request.POST.get('remark')

    if is_empty(menu_name):
        return error_handler('菜单名称不能为空')
    if is_empty(menu_path):
        return error_handler('菜单路径不能为空')
    if menu_type_id == 0:
        return error_handler('请输入menu_type_id')
    # 菜单类型判断
    menu_type = MenuManageType.objects.filter(id=menu_type_id)
    if menu_type is None or menu_type.__len__() == 0:
        return error_handler('菜单类型不正确')
    # 菜单是否存在判断
    menu_manage = MenuManage.objects.filter(id=menu_id)
    if menu_manage is None or menu_manage.__len__() == 0:
        return add_menu(menu_name, menu_path, menu_type_id, remark)
    else:
        return edit_menu(menu_manage[0], menu_name, menu_path, menu_type_id, remark)


# 新增菜单
def add_menu(menu_name, menu_path, menu_type_id, remark):
    exist_menu_name = is_exist_menu_name(menu_name)
    if exist_menu_name is not None:
        return exist_menu_name
    exist_menu_path = is_exist_menu_path(menu_path)
    if exist_menu_path is not None:
        return exist_menu_path
    menu_manage = MenuManage.objects.create(menu_name=menu_name, menu_path=menu_path, menu_type_id=menu_type_id,
                                            remark=remark)
    return result_handler(data=menu_manage.__str__())


# 修改菜单
def edit_menu(menu_manage, menu_name, menu_path, menu_type_id, remark):
    if menu_manage.menu_name != menu_name:
        exist_menu_name = is_exist_menu_name(menu_name)
        if exist_menu_name is not None:
            return exist_menu_name

    if menu_manage.menu_path != menu_path:
        exist_menu_path = is_exist_menu_path(menu_path)
        if exist_menu_path is not None:
            return exist_menu_path

    menu_manage.menu_name = menu_name
    menu_manage.menu_path = menu_path
    menu_manage.menu_type_id = menu_type_id
    menu_manage.remark = remark
    menu_manage.save()
    return result_handler(data=menu_manage.__str__())


# 判读菜单名是否存在
def is_exist_menu_name(menu_name):
    menu = MenuManage.objects.filter(menu_name=menu_name)
    if menu is not None and menu.__len__() > 0:
        return error_handler("菜单名称已经存在")
    else:
        return None


# 判读菜单路径是否存在
def is_exist_menu_path(menu_path):
    menu = MenuManage.objects.filter(menu_path=menu_path)
    if menu is not None and menu.__len__() > 0:
        return error_handler("菜单路径已经存在")
    else:
        return None


# 删除菜单名称
def delete_menu(request):
    menu_id = int(request.POST.get('id')) if request.POST.get('id') is not None else 0
    find_menu = MenuManage.objects.filter(id=menu_id)
    if find_menu is None or find_menu.__len__() == 0:
        return error_handler("菜单不存在")
    MenuManage.objects.filter(id=menu_id).delete()
    return result_handler(data=None)
