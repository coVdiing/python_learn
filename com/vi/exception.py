# _*_ coding:UTF-8 _*_

def caculate(num):
    return 10 / num


def temp_convert(value):
    try:
        return int(value)
    except ValueError, args:
        print '参数没有包含数字:', args


def throw_exception(level):
    if level < 0:
        raise Exception, "Invaild level"


try:
    result = caculate(10)
except Exception:
    print '捕获到异常'
except ZeroDivisionError:
    print '0不可以作为除数'
else:
    print '运算成功:', result
finally:
    print '程序结束!'

temp_convert('xyz')

print '-------主动抛出异常---------'

try:
    throw_exception(-1)
except Exception, args:
    print '捕获到异常:', args
