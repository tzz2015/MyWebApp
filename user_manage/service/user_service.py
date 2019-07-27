from django.contrib.auth import logout
from MyWebApp.json_utils import result_handler, error_handler
from ..base_service import user_base_service
from ..models import UserInfo

"""
用户业务处理逻辑
"""


# 用户登录逻辑
def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or username == '':
        return error_handler('请输入用户名')
    if password is None or password == '':
        return error_handler('请输入密码')
    user = user_base_service.user_auth(username, password)
    return user_base_service.user_login(request, user)


# 用户信息
def get_user_info(request):
    user = user_base_service.get_user_info(request)
    if user is None:
        return error_handler('用户不存在')
    return result_handler(user)


# 退出登录
def user_logout(request):
    logout(request)
    return result_handler('退出登录成功')


# 修改密码
def change_password(request):
    new_password = request.POST.get('newPassword')
    old_password = request.POST.get('oldPassword')
    if new_password is None or new_password == '':
        return error_handler('请输入新密码')
    if old_password is None or old_password == '':
        return error_handler('请输入旧密码')
    user = user_base_service.get_user_info(request)
    auth_user = user_base_service.user_auth(user.username, old_password)
    if auth_user is None:
        return error_handler('旧密码不匹配')
    change_user = user_base_service.user_change_password(auth_user, new_password)
    return result_handler(change_user)


# 获取系统用户列表
def get_user_list(request):
    page = request.POST.get('page', default=1)
    page_size = request.POST.get('page_size', default=10)
    filters = {}
    username = request.POST.get('username')
    user_type = request.POST.get('user_type')
    is_active = request.POST.get('is_active')
    if username is not None and username != '':
        filters['username__icontains'] = username
    if user_type is not None and user_type != '' and user_type != '-1':
        filters['user_type'] = int(user_type)
    if is_active is not None and is_active != '':
        filters['is_active'] = True if (is_active == 'true') else False
    return user_base_service.page_user(request, page, page_size, filters=filters)


# 获取系统用户列表
def create_or_update_user(request):
    user_id = int(request.POST.get('id', default=1))
    username = request.POST.get('username', default='刘宇飞')
    password = request.POST.get('password', default='lyf')
    user_type = int(request.POST.get('user_type', default=0))
    if user_id > 0:
        curr_user = UserInfo.objects.filter(id=user_id)
        if curr_user is None:
            return error_handler('用户不存在')
        name_user = UserInfo.objects.filter(username=username)
        if name_user.__len__() > 0 and name_user[0].id != user_id:
            return error_handler('用户名已经存在')
        if password is not None:
            user_base_service.user_change_password(curr_user[0], password)
        return user_base_service.update_sys_user(user_id, username=username, user_type=user_type)
    else:
        return user_base_service.create_sys_user(username, password, user_type)
