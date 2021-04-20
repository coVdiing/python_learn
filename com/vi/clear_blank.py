# coding:utf-8
import re
filename = 'f:/appendix.txt'
with open(filename) as file:
    lines = file.readlines()

result = []
for line in lines:
    if re.match('(\d+)\s*',line):
        line = line.split('\n')[0]
    elif line.startswith('\n'):
        continue
    result.append(line)


content = " ".join(result)
print(content)

filename = "f:/new_appendix.txt"
with open(filename,'w') as file:
    file.write(content)