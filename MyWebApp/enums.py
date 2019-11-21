from enum import Enum


class UserType(Enum):
    # 用户角色 0：超级管理员，1：管理员 2：普通用户
    SUPER = 0
    MANAGE = 1
    OTHER = 2


class PayType(Enum):
    # 支付状态
    NO_PAY = 0
    PAY_ED = 1
    AUDIT = 2
