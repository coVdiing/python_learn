# _*_ coding:UTF-8 _*_
def write_number(test_file):
    for i in range(1, 100):
        test_file.write("{}\n".format(i ** 2))
    test_file.close()

test_file = open("foo.txt", "r+")
print '文件名:', test_file.name
print '是否已关闭: ',test_file.closed
print '访问模式: ',test_file.mode

str = test_file.read()
print '重新读取字符串:\n',str





