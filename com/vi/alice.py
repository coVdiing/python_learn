# coding:UTF-8
filename = 'alice.txt'

try:
    with open(filename) as f:
        content = f.read()
except IOError:
    print "文件{}不存在!".format(filename)
else:
    words = content.split()
    num_words = len(words)
    print "文件{} 有大约{}个词".format(filename,num_words)