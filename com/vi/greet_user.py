# coding:UTF-8
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print('欢迎回来,{}'.format(username))