from django.urls import path
import user_manage.views as views
import user_manage.handler.user_handler as user_handler
import user_manage.handler.alum_handle as alum_handle
from user_manage.handler.upload_tenxun_handler import upload_tenxun_file

urlpatterns = [
    path('', views.hello),
    path('upload_file', upload_tenxun_file),
    path('login', user_handler.login),
    path('user_info', user_handler.get_user),
    path('logout', user_handler.logout),
    path('change_password', user_handler.change_password),
    path('user_list', user_handler.user_list),
    path('create_update_user', user_handler.create_or_update_user),
    path('active', user_handler.active),
    path('delete_user', user_handler.delete_user),
    path('alum_list', alum_handle.alum_list),
    path('edit_alum', alum_handle.edit_alum),
    path('alum_order_list', alum_handle.alum_order_list),
    path('update_alum_order', alum_handle.update_alum_order),
    path('alum_order_detail', alum_handle.get_alum_order),

]
not_need_login = [
    views.hello,
    user_handler.login,
    user_handler.create_or_update_user,
]
