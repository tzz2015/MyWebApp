from MyWebApp.json_utils import result_handler, error_handler
from django.contrib.auth import authenticate, get_user, logout, login, update_session_auth_hash
from ..models import UserInfo
from django.core.cache import cache
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


def user_all(request):
    user_list = UserInfo.objects.all()
    return result_handler(user_list)


# 修改密码
def user_change_password(auth_user, new_password):
    if auth_user is None:
        return error_handler('旧密码不匹配')
    auth_user.set_password(new_password)
    auth_user.save()
    return result_handler(auth_user)
