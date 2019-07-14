"""
登录拦截
"""

from django.utils.deprecation import MiddlewareMixin
from ..urls import not_need_login
from ..json_utils import result_handler


class LoginMiddleware(MiddlewareMixin):

    # 中间件函数。(用到哪个函数写哪个，不需要全写)
    def process_request(self, request):
        """产生request对象之后，url匹配之前调用"""
        print('请求方法：%s \n请求参数：%s' % (request.method, request.content_params))

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """匹配需要拦截的方法，判断是否登录"""
        print('方法名:%s' % view_func)
        if not not_need_login.__contains__(view_func):
            user = request.user
            if user is None or not request.user.is_authenticated:
                return result_handler(None, msg='用户没有登录', code=303)

    def process_response(self, request, response):
        """视图函数调用之后，response返回浏览器之前"""
        print('返回数据：%s' % str(response.content, encoding="utf8").encode('utf-8').decode('unicode_escape'))

        return response  # 一般会返回响应。
