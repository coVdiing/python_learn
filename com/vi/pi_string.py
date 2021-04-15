# coding:UTF-8
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = raw_input("输入生日: ")
if birthday in pi_string:
    print "生日在圆周率中出现了"
else:
    print "生日没有在圆周率中出现"

