# -*- coding:utf-8 -*
import time
import  calendar
ticks = time.time()
print ticks

print '本地时间为:',time.localtime(time.time())

print '格式化时间:',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

print calendar.month(2021,4)

