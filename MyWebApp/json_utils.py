from django.db.models import QuerySet
from django.http import HttpResponse
import json
import datetime
from django.forms.models import model_to_dict
from django.db import models


# 返回统一的json格式
def result_handler(data, msg='ok', code=200):
    data = format_data(data)
    model = BaseModel(data=data, msg=msg, code=code)
    return HttpResponse(json.dumps(model.to_dict(), cls=DateEncoder), content_type="application/json", )


# 统一字抛错误
def error_handler(msg):
    return result_handler(data=None, msg=msg, code=201)


# 将QuerySet转换成list 或者将model转换成dict
# 解决无法正常格式化问题
def format_data(data):
    # 将model转换成dict
    if isinstance(data, models.Model):
        data = model_to_dict(data)
    if type(data) is QuerySet:
        back_data = []
        for item in data:
            if isinstance(item, models.Model):
                back_data.append(model_to_dict(item))
            else:
                back_data.append(item)
        if back_data.__len__() > 0:
            data = back_data

    return data


class BaseModel(object):
    def __init__(self, data, msg='ok', code=200):
        self.code = code
        if data is None:
            self.data = {}
        else:
            self.data = data
        self.msg = msg

    def to_dict(self):
        r = {
            'code': self.code,
            'data': self.data,
            'msg': self.msg,
        }
        return r


# 将datetime转换成字符串
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
