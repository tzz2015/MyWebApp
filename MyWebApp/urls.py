"""MyWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_manage import user_urls
from menu_manage import menu_urls
from .middleware.ExceptionMiddleware import page_error, page_not_found, permission_denied

urlpatterns = [
    path('admin/', admin.site.urls),
]
# 一个模块一个urlpatterns 各自管理
urlpatterns.extend(user_urls.urlpatterns)
urlpatterns.extend(menu_urls.urlpatterns)

not_need_login = []

# 一个模块一个not_need_login 各自管理
not_need_login.extend(user_urls.not_need_login)
not_need_login.extend(menu_urls.not_need_login)

handler403 = permission_denied
handler404 = page_not_found
handler405 = permission_denied
handler500 = page_error
