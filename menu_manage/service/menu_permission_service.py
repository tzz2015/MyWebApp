from MyWebApp.json_utils import result_handler, error_handler, format_data
from MyWebApp.utils import is_empty
from menu_manage.models import UserMenuPermission
from user_manage.base_service.user_base_service import get_user_info


# 查询菜单权限列表
def get_menu_permission_list(request):
    user = get_user_info(request)
    permission_list = UserMenuPermission.objects.filter(user_id=user.id).all()
    return result_handler(permission_list)
