def firstAlpha(S):
    S=S.split()
    res=''
    for i in S:
        res+=i[0]
    return res


print(firstAlpha("bad is good"))

