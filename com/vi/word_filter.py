# _*_ coding:utf-8 _*_

if __name__ == '__main__':
    with open("invalid_word.txt", encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        if lines[i].endswith('\n'):
            items = lines[i].split('\n')
            lines[i] = items[0]
    while True:
        line = input('input:')
        if line == 'quit':
            break
        for item in lines:
            if line.__contains__(item):
                line = line.replace(item, '*')
        print(line)