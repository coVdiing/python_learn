# _*_ coding:UTF-8 _*_
import os

print [x for x in os.listdir('.') if os.path.isfile(x)]

print [x for x in os.listdir('.') if  os.path.isdir(x)]