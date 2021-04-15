def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def trim(s):
    length = len(s)
    for i in range(0,length):
        if s[i] == ' ':
            continue
        else:
            start = i
            break
    for i in range(start+1,length):
        if s[i] != ' ':
            continue
print fact(1)
print fact(5)
print fact(100)

