"""
相册操作
"""

import user_manage.service.alum_server as service


# 获取相册分页列表
def alum_list(request):
    return service.get_alum_list(request)


# 获取相册分页列表
def alum_order_list(request):
    return service.get_alum_list(request)


# 新增或者编辑相册
def edit_alum(request):
    return service.edit_alum(request)


# 修改订单状态
def update_alum_order(request):
    return service.update_alum_order(request)
