import hashlib
import time

from MyWebApp.enums import UserType, PayType
from MyWebApp.json_utils import result_handler, error_handler
from user_manage.base_service.user_base_service import get_user_info

from user_manage.models import AlumModel, PayModel


# 获取相册列表
def get_alum_list(request):
    menu_list = PayModel.objects.all().order_by('createTime')
    return result_handler(menu_list)


# 获取相册列表
def get_alum_order_list(request):
    menu_list = AlumModel.objects.all().order_by('createTime')
    return result_handler(menu_list)


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
    PayModel.objects.filter(alum_id=key).update(pay_status=pay_status)
    return result_handler(key)
