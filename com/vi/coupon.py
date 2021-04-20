# _*_ coding:UTF-8 _*_
# 生成200个优惠券,时间戳加随机数
import random
import time
import uuid


def generate_coupon(number):
    coupon_list = []
    for i in range(0,number):
        coupon_list.append(''.join(str(uuid.uuid4()).split('-')))
    return coupon_list

# print(generate_coupon(200))

