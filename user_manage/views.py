# Create your views here.
from MyWebApp.json_utils import result_handler
from django.contrib.auth import authenticate, login, logout


def hello(request):
    return result_handler('Hello Word!')


def user_login(request):
    username = 'lyf'
    password = 'lyf'
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return result_handler('登录成功！')
    else:
        return result_handler('用户名或者密码错误')


def user_logout(request):
    logout(request)
    return result_handler('退出登录成功')
