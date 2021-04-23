# _*_ coding:UTF-8 _*_
"""生成30个txt，用指定词库随机填充内容"""
import random
import os
import re

list = ['peace', 'love', 'world', 'game', 'lol', 'basketball', 'girl', 'boy', 'nation', 'country', 'city', 'family',
        'mother', 'parent'
    , 'dream', 'job', 'hobby', 'book', 'novel', 'science', 'universary', 'high', 'school', 'age', 'skin', 'China',
        'chinese', 'friend',
        'some say love', 'it is a river', 'it\'s been a long time', 'you raise me up', 'leamon tree',
        'you don\'t have to try so hard']

def write_diary():
    filepath = 'F:/diary'

    for i in range(0, 30):
        filename = "{}/diary-{}.txt".format(filepath, i)
        with open(filename, 'a') as file:
            for i in range(0, 10):
                index = random.randint(0, len(list))
                print(index)
                file.write(list[index%len(list)] + "\n")

def analyse_diary():
    filepath = 'F:/diary'
    list = os.listdir(filepath)
    # 准备一个字典存放词汇
    word_dict = {}
    pattern = re.compile('[\w+\'*]+')
    for item in list:
        filename = filepath+'/'+item
        if filename.endswith('.txt'):
            with open(filename,'rb') as file:
                content = file.read()
                content = content.decode('utf-8')
                word_list =  re.findall(pattern,content)
                for word in word_list:
                    if word not in word_dict.keys():
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
    print(word_dict)
    max_key = ""
    max_value = 0
    for key,value in word_dict.items():
        if value > max_value:
            max_key = key
            max_value = value
    print("最重要的词是:{},次数:{}".format(max_key,max_value))
# write_diary()
analyse_diary()