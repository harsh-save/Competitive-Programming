def strstr(s,x):
    if (x in s):
        return s.index(x)
    return -1

print(strstr('GeeksForGeeks','For'))
