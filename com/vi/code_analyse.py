# _*_ coding:UTF-8 _*_
import re
import os


def analyse_file(filename, dict):
    pattern1 = re.compile('#[*\w*\s*]*')
    pattern2 = re.compile('\\n')
    pattern3 = re.compile('[\w*\s*:(*)*1-9*]+')

    with open(filename, encoding='UTF-8') as file:
        lines = file.readlines()
    for line in lines:
        if re.match(pattern1, line):
            dict['others'].append(line)
        elif re.match(pattern2, line):
            dict['blanks'].append(line)
        elif re.match(pattern3, line):
            dict['codes'].append(line)
        else:
            print("没找到匹配模式:"+line)




if __name__ == '__main__':
    dict = {
        "others": [],
        "blanks": [],
        "codes": []
    }
    filepath = './'
    file_list = os.listdir(filepath)
    pys = []
    for file in file_list:
        if file.endswith('.py'):
            pys.append(file)
            analyse_file(filepath+file,dict)
    # analyse_file('10-8.py',dict)

    print(len(pys))
    print('注释:{}行', len(dict['others']))
    print('空白:{}行', len(dict['blanks']))
    print('代码:{}行', len(dict['codes']))

