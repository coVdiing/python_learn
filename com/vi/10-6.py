# coding:UTF-8

while True:
    print "给我两个数,我来求和，输入q退出程序"
    first_num = raw_input('\n第一个数: ')
    if first_num == 'q':
        break
    second_num = raw_input('\n第二个数: ')
    if second_num == 'q':
        break
    try:
        sum = float(first_num) + float(second_num)
    except ValueError:
        print '输入的数格式不正确'
    else:
        print sum