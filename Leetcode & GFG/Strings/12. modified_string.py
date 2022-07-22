def modStr(s):
    s=list(s)
    count=0
    for i in range(1,len(s)):
        if(i+1<len(s) and i-1>0):
            if(s[i]==s[i-1] and s[i+1]==s[i]):
                count+=1
    return count


print(modStr('aaa'))

