from django.urls import path
import menu_manage.handler.menu_type_handler as menu_type
import menu_manage.handler.menu_handler as menu
import menu_manage.handler.menu_permission_handler as menu_permission

urlpatterns = [
    path('menu_type_list', menu_type.get_menu_type_list),
    path('create_menu_type', menu_type.create_menu_type),
    path('delete_menu_type', menu_type.delete_menu_type),
    path('menu_list', menu.get_menu_list),
    path('menu_list_by_type', menu.get_menu_list_by_type),
    path('add_or_edit_menu', menu.add_or_edit_menu),
    path('delete_menu', menu.delete_menu),
    path('permission_menu_list', menu_permission.get_user_menu_permission_list),
    path('delete_permission_menu', menu_permission.delete_menu_permission),
    path('add_permission_menu', menu_permission.add_menu_permission),
    path('add_batch_menu_permission', menu_permission.add_batch_menu_permission),

]
not_need_login = [

]
