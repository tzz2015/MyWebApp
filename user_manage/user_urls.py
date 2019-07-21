from django.urls import path
import user_manage.views as views
import user_manage.handler.user_handler as user_handler

urlpatterns = [
    path('', views.hello),
    path('login', user_handler.login),
]
not_need_login = [
    views.hello,
    user_handler.login,

]
