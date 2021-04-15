# _*_ coding:UTF-8 _*_
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print "{} is now sitting ".format(self.name)

    def roll_over(self):
        print "{} is now rolled over".format(self.name)


my_dog = Dog('tom',6)
my_dog.sit()
my_dog.roll_over()
print my_dog.name
print my_dog.age