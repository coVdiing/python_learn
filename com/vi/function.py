# -*- coding:UTF-8 -*
# 定义一个函数,方法的命名用帕斯卡命名法
import time
import calendar

def print_double(str):
    print str * 2
    return str * 2


def build_person(first_name, last_name, age=None):
    person = {
        'first_name': first_name,
        'last_name': last_name
    }
    if age:
        person['age'] = age
    return person


def favorite_book(title):
    print("我最喜欢的书是:{}".format(title))


def make_ablum():
    active = True
    while active:
        author = raw_input("请输入歌手名: ")
        if author == 'quit':
            active = False
            continue
        ablum_name = raw_input("请输入专辑名: ")
        if ablum_name == 'quit':
            active = False
            continue
        ablum = {
            'author': author,
            'ablum_name': ablum_name
        }
        for key, value in ablum.items():
            print key," -> ",value


def show_month():
    print calendar.month(2021,4)

def show_time():
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


#
# favorite_book("七夜雪")
#
# print print_double('vi')
#
# print(build_person('li', 'jiawei', 26))

# make_ablum()

# show_month()

# show_time()