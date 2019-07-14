from django.urls import path
import user_manage.views as views

urlpatterns = [
    path('', views.hello),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('user_list', views.user_all),
]
not_need_login = [
    views.hello,
    views.user_login,
]
