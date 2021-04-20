# _*_ coding:UTF-8 _*_
"""任一个英文的纯文本文件，统计其中的单词出现的个数"""
import re

filename = './alice.txt'
with open(filename,'rb') as file:
    content = file.read()
content = content.decode('utf-8')
pattern = re.compile('\w+')
target = pattern.findall(content)
result = []
# target2 = pattern.findall(content)

for item in target:
    if item.strip() not in result:
        result.append(item)

# 30537
print(result)
