# coding:UTF-8
catfile = 'cat.txt'
dogfile = 'dig.txt'

def read_file(list):
    for item in list:
        print item
        with open(item) as file_object:
            lines = file_object.readlines()
        for line in lines:
            print line.rstrip()

list = [catfile,dogfile]

try:
    read_file(list)
except IOError:
    pass

# with open(catfile) as file_object:
#     print file_object.read()