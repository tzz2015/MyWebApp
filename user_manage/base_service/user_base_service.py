from MyWebApp.enums import UserType
from MyWebApp.json_utils import result_handler, error_handler, format_data
from django.contrib.auth import authenticate, get_user, logout, login
from MyWebApp.utils import page_list
from menu_manage.service.base_menu_server import add_permission_by_name
from ..models import UserInfo

"""
用户基础逻辑
"""


# 用户验证
def user_auth(username, password):
    return authenticate(username=username, password=password)


# 用户登录
def user_login(request, user):
    if user is None:
        return error_handler('账号或者密码错误')
    login(request, user)
    return result_handler(user)


# 获取当前用户信息
def get_user_info(request):
    return get_user(request)


def user_logout(request):
    logout(request)
    return result_handler('退出登录成功')


# 分页用户
def page_user(request, page, page_size, filters=None):
    # exclude = {'is_superuser': True}
    user_page = page_list(page, page_size, UserInfo, filter=filters)
    user_list = user_page.get('list')
    for user in user_list:
        if user['user_type'] != 0:
            from menu_manage.service.menu_permission_service import get_menu_list_by_user
            menu_list = get_menu_list_by_user(user['id'])
            user['menu_list'] = menu_list
        else:
            user['menu_list'] = []
    return result_handler(user_page)


# 修改密码
def user_change_password(auth_user, new_password):
    auth_user.set_password(new_password)
    auth_user.save()
    return auth_user


# 创建用户
def create_sys_user(username, password, user_type=2):
    find_user = UserInfo.objects.filter(username=username)
    if find_user.__len__() > 0:
        return error_handler('用户名已经存在')
    user = UserInfo.objects.create_user(username=username, email=None, user_type=user_type)
    if user is None:
        return error_handler('创建用户失败')
    user_change_password(user, password)
    # 添加默认的菜单权限
    add_default_menu_permission(user)
    return result_handler(user)


# 更新用户
def update_sys_user(user_id, **kwargs):
    rows = UserInfo.objects.filter(id=user_id).update(**kwargs)
    if rows == 0:
        return error_handler('更新失败')
    return result_handler('更新成功')


# 删除用户
def delete_user(user_id):
    rows = UserInfo.objects.filter(id=user_id).delete()
    if rows == 0:
        return error_handler('删除失败')
    return result_handler('删除成功')


# 根据ID查找用户
def find_user_by_id(user_id):
    return UserInfo.objects.filter(id=user_id)


# 增加默认的菜单权限
def add_default_menu_permission(user):
    if user.user_type == UserType.SUPER.value:
        return -1
    menu_name_list = ['相册列表']
    for item in menu_name_list:
        add_permission_by_name(user.id, item)
