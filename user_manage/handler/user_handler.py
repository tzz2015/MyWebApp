import user_manage.service.user_service as user
from django.views.decorators.http import require_POST
"""
用户接口统一入口
"""


# 用户登录
@require_POST
def login(request):
    return user.do_login(request)
