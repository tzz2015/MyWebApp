from django.urls import path
import menu_manage.handler.menu_type_handler as menu_type
import menu_manage.handler.menu_handler as menu

urlpatterns = [
    path('menu_type_list', menu_type.get_menu_type_list),
    path('create_menu_type', menu_type.create_menu_type),
    path('delete_menu_type', menu_type.delete_menu_type),
    path('menu_list', menu.get_menu_list),
    path('add_or_edit_menu', menu.add_or_edit_menu),
    path('delete_menu', menu.delete_menu),
]
not_need_login = [

]
