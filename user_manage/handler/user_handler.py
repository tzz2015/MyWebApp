import user_manage.service.user_service as user
from django.views.decorators.http import require_POST

"""
用户接口统一入口
"""


# 用户登录
@require_POST
def login(request):
    return user.do_login(request)


# 用户信息
def get_user(request):
    return user.get_user_info(request)


# 退出登录
def logout(request):
    return user.user_logout(request)


# 修改密码
def change_password(request):
    return user.change_password(request)


# 获取用户列表
def user_list(request):
    return user.get_user_list(request)


# 创建或者更新用户
def create_or_update_user(request):
    return user.create_or_update_user(request)
