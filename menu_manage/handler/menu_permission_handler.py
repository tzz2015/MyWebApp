from menu_manage.service import menu_permission_service as permissionServer


# 查询用户的权限列表
def get_user_menu_permission_list(request):
    return permissionServer.get_menu_permission_list(request)
