from MyWebApp.json_utils import result_handler
from django.contrib.auth import authenticate, login, logout
from ..models import UserInfo

"""
用户基础逻辑
"""


def user_login(username, password):
    return authenticate(username=username, password=password)


def user_logout(request):
    logout(request)
    return result_handler('退出登录成功')


def user_all(request):
    user_list = UserInfo.objects.all()
    return result_handler(user_list)
