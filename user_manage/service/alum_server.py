import hashlib
import time

from MyWebApp.enums import UserType, PayType
from MyWebApp.json_utils import result_handler, error_handler, format_data
from MyWebApp.utils import page_list
from user_manage.base_service.user_base_service import get_user_info, find_user_by_id

from user_manage.models import AlumModel, PayModel, UserInfo


# 获取相册列表
def get_alum_list(request):
    user = get_user_info(request)
    page = request.POST.get('page', default=-1)
    page_size = request.POST.get('page_size', default=10)
    filters = {}
    username = request.POST.get('username')
    if username is not None and username != '':
        filters['user__username__contains'] = username
    if user.user_type == UserType.OTHER.value:
        filters['user_id'] = user.id
    search_list = page_list(page, page_size, AlumModel, filter=filters)
    for item in search_list['list']:
        item['user'] = find_user_by_id(item['user']).values()[0]
        pay_info = PayModel.objects.filter(alum_id=item['key']).values()
        item['alum'] = pay_info[0] if pay_info.__len__() > 0 else {}

    return result_handler(search_list)


# 获取相册列表
def get_alum_order_list(request):
    page = request.POST.get('page', default=-1)
    page_size = request.POST.get('page_size', default=10)
    filters = {}
    username = request.POST.get('username')
    if username is not None and username != '':
        filters['user__username__contains'] = username
    search_list = page_list(page, page_size, PayModel, filter=filters)
    for item in search_list['list']:
        item['user'] = find_user_by_id(item['user']).values()[0]
    return result_handler(search_list)


# 获取相册列表
def edit_alum(request):
    user = get_user_info(request)
    key = request.POST.get('key')
    bg_url = request.POST.get('bg_url')
    music_url = request.POST.get('music_url')
    image_urls = request.POST.get('image_urls')
    if bg_url is None or bg_url == '':
        return error_handler('请添加背景图片')
    if music_url is None or music_url == '':
        return error_handler('请添加音乐')
    if image_urls is None or image_urls == '':
        return error_handler('请添加相册图片')
    if key is None or key == '':
        key = hashlib.md5(str(int(round(time.time() * 1000))).encode(encoding='UTF-8')).hexdigest()
        AlumModel.objects.create(user_id=user.id, bg_url=bg_url, music_url=music_url, image_urls=image_urls,
                                 key=key)
        create_order(user, key)
    else:
        AlumModel.objects.filter(key=key).update(user_id=user.id, bg_url=bg_url, music_url=music_url,
                                                 image_urls=image_urls)

    return result_handler(key)


# 创建订单
def create_order(user, key):
    pay_status = PayType.NO_PAY.value
    try:
        if user.user_type == UserType.SUPER.value or user.user_type == UserType.MANAGE.value:
            pay_status = PayType.PAY_ED.value
        PayModel.objects.create(alum_id=key, pay_status=pay_status, user_id=user.id)
    except Exception as e:
        print(e)


# 修改相册订单
def update_alum_order(request):
    key = request.POST.get('key')
    pay_status = int(request.POST.get('pay_status', default=0))
    user = get_user_info(request)

    if (
            pay_status == PayType.NO_PAY.value or pay_status == PayType.PAY_ED.value) and user.user_type != UserType.SUPER.value:
        return error_handler('只有管理员才有权限修改')
    if pay_status == PayType.AUDIT.value:
        pay = PayModel.objects.filter(alum_id=key)
        if pay.__len__() > 0 and user.id != pay[0].user_id:
            return error_handler('你无权提交')
    PayModel.objects.filter(alum_id=key).update(pay_status=pay_status)
    return result_handler(key)


# 获取订单详情
def get_alum_order(request):
    key = request.POST.get('key')
    return result_handler(PayModel.objects.filter(alum_id=key).values())
