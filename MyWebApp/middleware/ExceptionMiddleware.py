"""
定义中间件类，处理全局异常
"""
from django.utils.deprecation import MiddlewareMixin
from ..json_utils import result_handler


class ExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        print('----捕获到异常----')
        print(exception)
        return result_handler(None, msg='系统异常，请联系管理员', code=500)


"""全局403、404、500错误自定义页面显示"""


def page_not_found(request, exception):
    return result_handler(None, msg='接口不存在', code=404)


def page_error(request):
    return result_handler(None, msg='系统异常，请联系管理员', code=500)


def permission_denied(request, exception):
    return result_handler(None, msg='没有权限', code=400)
