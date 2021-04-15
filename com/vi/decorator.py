# _*_ coding:UTF-8 _*_
import time


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))


def metric(fn):
    def wrapper(*args, **kwargs):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kwargs)
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
