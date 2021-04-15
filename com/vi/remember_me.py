# coding:UTF-8
import json
filename = 'username.json'
username = raw_input('输入你的用户名:')
with open(filename,'w') as f:
    json.dump(username,f)
    print("你下次来的时候还会记住你,{}".format(username))