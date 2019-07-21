from django.contrib.auth import authenticate, login, logout
from MyWebApp.json_utils import result_handler
from ..base_service import user_base_service

"""
用户业务处理逻辑
"""


# 用户登录逻辑
def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or username == '':
        return result_handler(None, '请输入用户名', 201)
    if password is None or password == '':
        return result_handler(None, '请输入密码', 201)
    user = user_base_service.user_login(username, password)
    if user is None:
        return result_handler(None, '账号或者密码错误', 201)
    login(request, user)
    return result_handler(user)
