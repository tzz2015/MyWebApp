from django.urls import path
import user_manage.views as views
import user_manage.handler.user_handler as user_handler

urlpatterns = [
    path('', views.hello),
    path('login', user_handler.login),
    path('user_info', user_handler.get_user),
    path('logout', user_handler.logout),
    path('change_password', user_handler.change_password),
    path('user_list', user_handler.user_list),
    path('create_update_user', user_handler.create_or_update_user)

]
not_need_login = [
    views.hello,
    user_handler.login,

]
