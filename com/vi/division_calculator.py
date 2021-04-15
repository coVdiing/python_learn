# coding:UTF-8
print '给我两个数，我来做除法'
print '输入q退出程序'

while True:
    first_number = raw_input('\n First Number: ')
    if first_number == 'q':
        break
    second_number = raw_input('\n Second Number: ')
    if second_number == 'q':
        break
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print "零不能作为除数"
    else:
        print answer
