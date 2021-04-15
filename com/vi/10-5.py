# coding:UTF-8
filename = 'reason.txt'
while True:
    reason = raw_input("你为什么喜欢编程? ")
    if reason == 'quit':
        break
    with open(filename,'a') as file_object:
        file_object.write("{}\n".format(reason))
