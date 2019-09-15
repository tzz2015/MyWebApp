from django.urls import path
import menu_manage.handler.menu_type_handler as content

urlpatterns = [
    path('menu_type_list', content.get_menu_type_list),
    path('create_menu_type', content.create_menu_type),
    path('delete_menu_type', content.delete_menu_type),

]
not_need_login = [

]
