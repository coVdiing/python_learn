# _*_ coding:UTF-8 _*_

class Student(object):
    def __init__(self,name,gender):
        self.__gender = gender
        self.__name = name

    def set_gender(self,gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
