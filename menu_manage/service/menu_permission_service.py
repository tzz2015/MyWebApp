import logging

from MyWebApp.json_utils import result_handler, error_handler, format_data
from menu_manage.models import UserMenuPermission, MenuManage, MenuManageType
from menu_manage.service.base_menu_server import add_permission
from menu_manage.service.menu_service import get_menu_list_by_type
from user_manage.base_service.user_base_service import get_user_info, find_user_by_id

logger = logging.getLogger('menu_permission_handler')


# 查询用户菜单权限列表
def get_menu_permission_list(request):
    user = get_user_info(request)
    if user.user_type == 0:
        return get_menu_list_by_type()
    else:
        return get_not_supper_menu_list(user)


# 非管理员用户菜单列表
def get_not_supper_menu_list(user):
    return result_handler(get_menu_list_by_user(user.id))


# 根据用户获取用户拥有的菜单
def get_menu_list_by_user(user_id):
    permission_list = UserMenuPermission.objects.filter(user_id=user_id)
    menu_ids = []
    for permission in permission_list:
        menu_ids.append(permission.menu.id)

    menu_type = list(MenuManageType.objects.all().values())
    menu = []
    for item in menu_type:
        menu_list = MenuManage.objects.filter(menu_type_id=item['id'], pk__in=menu_ids).all()
        if menu_list.__len__() != 0:
            item['menu_list'] = format_data(menu_list)
            menu.append(item)
    return menu


# 删除用户的权限菜单
def delete_menu_permission(request):
    menu_id = request.POST.get('menu_id')
    user_id = request.POST.get('user_id')
    r, v = UserMenuPermission.objects.filter(menu_id=menu_id, user_id=user_id).delete()
    if r == 1:
        return result_handler(None)
    else:
        return error_handler('删除失败')


# 新增用户的权限菜单
def add_menu_permission(request):
    menu_id = request.POST.get('menu_id')
    user_id = request.POST.get('user_id')
    # 判断菜单是否存在
    menu = MenuManage.objects.filter(id=menu_id).all()
    if menu.__len__() == 0:
        return error_handler('菜单不存在')
    user = find_user_by_id(user_id)
    if user.__len__() == 0:
        return error_handler('用户不存在')
    exit_permission = UserMenuPermission.objects.filter(menu_id=menu_id, user_id=user_id)
    if exit_permission.__len__() != 0:
        return error_handler('权限已经存在')
    UserMenuPermission.objects.create(menu_id=menu_id, user_id=user_id)
    return result_handler(None)


# 批量给用户添加权限
def add_batch_menu_permission(request):
    user_id = int(request.POST.get('id', default=-1))
    menu_ids = request.POST.get('menuIds')
    if menu_ids is None:
        return error_handler('menuIds必须存在')
    menu_ids = menu_ids.split(',')
    user = find_user_by_id(user_id)
    if user.__len__() == 0:
        return error_handler('用户不存在')
    add_menu_ids = []
    for menu_id in menu_ids:
        result_id = add_permission(user_id, menu_id)
        if result_id > 0:
            add_menu_ids.append(result_id)
    per_list = UserMenuPermission.objects.filter(user_id=user_id)
    for permission in per_list:
        if str(permission.menu_id) not in menu_ids:
            UserMenuPermission.objects.filter(user_id=user_id, menu_id=permission.menu_id).delete()
    return result_handler(add_menu_ids)



