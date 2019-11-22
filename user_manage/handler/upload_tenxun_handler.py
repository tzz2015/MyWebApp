# -*- coding=utf-8
import datetime
import re
import time
import os
from io import BytesIO

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import requests
import sys
import logging

from MyWebApp import settings
from MyWebApp.json_utils import result_handler, error_handler, format_data

# 腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7以及Python3.x

# pip安装指南:pip install -U cos-python-sdk-v5

# cos最新可用地域,参照https://www.qcloud.com/document/product/436/6224
from MyWebApp.json_utils import is_empty

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = 'AKIDqThgV6LZcbZJpBHCrKkxwgHeqnU53heS'  # 替换为用户的secret_id
secret_key = 'iDYgZNuITTRBg14tX3OZYIIAq71kFco9'  # 替换为用户的secret_key
region = 'ap-chengdu'  # 替换为用户的region
token = None  # 使用临时密钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)
bucket = "tensee-1259402050"
host = 'https://tensee-1259402050.cos.ap-chengdu.myqcloud.com/'


# 查询存储桶列表
def search_buckets_list():
    response = client.list_buckets()
    print(response)


# 查询文件列表
def search_file_list():
    response = client.list_objects(
        Bucket=bucket)
    print(response['Contents'])


# 本地文件上传到腾讯云
def upload_file(paths):
    try:
        file_dir = time.strftime("%Y-%m-%d")
        (path, name) = os.path.split(paths)
        file_name = "WebApp/" + str(file_dir) + "/" + name
        response = client.upload_file(
            Bucket=bucket,
            LocalFilePath=paths,
            Key=file_name,
            PartSize=1,
            MAXThread=10,
            EnableMD5=False
        )
        print(response)
        return host + file_name
    except Exception as e:
        print(e)
        return ''


# 网络图片上传到腾讯云
def upload_net_file(request):
    try:
        url = request.POST.get('url')
        file_dir = time.strftime("%Y-%m-%d")
        (path, name) = os.path.split(url)
        file_name = "WebApp/" + str(file_dir) + "/" + name
        # 网络流将以 Transfer-Encoding:chunked 的方式传输到 COS
        stream = requests.get(url)
        response = client.put_object(
            Bucket=bucket,
            Body=stream,
            Key=file_name
        )
        return result_handler(host + file_name)
    except Exception as e:
        print(e)
        return error_handler(e)


# 按字节流上传到腾讯云 微信小程序以字节流方式上传
def upload_tenxun_file(request):
    try:
        file_dir = time.strftime("%Y-%m-%d")
        file = request.FILES.get("file")
        file_name = "WebApp/" + str(file_dir) + "/" + os.path.splitext(file.name)[0][-30:] + \
                    os.path.splitext(file.name)[1]
        buf = BytesIO()
        for chunk in file.chunks():
            buf.write(chunk)
        buf.seek(0)
        response = client.put_object(
            Bucket=bucket,
            Body=buf,
            Key=file_name,
            StorageClass='STANDARD',
            EnableMD5=False
        )
        return result_handler(host + file_name)
    except Exception as e:
        print(e)
        return error_handler(e)


if __name__ == '__main__':
    url = '../../media/upload/.mp3'
    upload_file(url)
