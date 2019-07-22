from django.contrib.auth import logout
from MyWebApp.json_utils import result_handler, error_handler
from ..base_service import user_base_service

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
    return user_base_service.user_change_password(auth_user, new_password)
