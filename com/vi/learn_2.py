# -*- coding: utf-8 -*

# 打印99乘法表
for i in range(1,10):
    for j in range(i,10):
        if j != 9:
            print "{} * {} = {} ".format(i, j, i * j),
        else:
            print "{} * {} = {}".format(i, j, i * j)