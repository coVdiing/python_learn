# _*_ coding: UTF-8 _*_

# def input_byraw():
#     while True:
#         str = raw_input("请输入\n")
#         if (str == 'quit'):
#             break
#         print str, "(#^.^#)"
#
# def input_byinput():
#     while True:
#         str = input("请输入(仅支持表达式),输入'quit'可以退出\n")
#         if (str == 'quit'):
#             break
#         print str, "^_^"

# input_byinput()

# input_byraw()

def read_book():
    file = 'f:/snow in 7 night.txt'
    # file = 'C:\\Users\\pc\\Downloads\\13841408089154.txt'
    with open(file, 'rb') as f:
        buffer = f.read()
        data = buffer.decode('utf-8')
    i = 0
    while i + 50 < len(data):
        flag = input('go?(y/n)')
        if flag == 'n':
            break
        print(data[i:i + 50])
        i += 50
    if flag != 'n' and i+50 > len(data):
        print(data[i:len(data)])


read_book()
