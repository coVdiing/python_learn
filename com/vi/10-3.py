# coding:UTF-8
name = raw_input("请输入用户名: ")
filename = 'guest.txt'

with open(filename,'a') as file_object:
    file_object.write("{}\n".format(name))