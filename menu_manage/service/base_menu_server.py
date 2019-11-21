import logging

from menu_manage.models import MenuManage, UserMenuPermission

logger = logging.getLogger('base_menu_server')


# 添加菜单权限
def add_permission(user_id, menu_id):
    # 判断菜单是否存在
    menu = MenuManage.objects.filter(id=menu_id).all()
    if menu.__len__() == 0:
        logger.error('菜单不存在')
        return -1
    exit_permission = UserMenuPermission.objects.filter(menu_id=menu_id, user_id=user_id)
    if exit_permission.__len__() != 0:
        logger.error('权限已经存在')
        return -1
    UserMenuPermission.objects.create(menu_id=menu_id, user_id=user_id)
    logger.error('权限添加成功')
    return int(menu_id)


# 根据权限名称添加权限
def add_permission_by_name(user_id, menu_name):
    menu = MenuManage.objects.filter(menu_name=menu_name).all()
    if menu.__len__() == 0:
        logger.error('菜单不存在')
        return -1
    return add_permission(user_id, menu[0].id)
