def isAnagram(a,b):
    seen={}
    if(len(a)!=len(b)):
        return False
    for i in a:
        if (i in seen):
            seen[i]+=1
        else:
            seen[i]=1
    for i in b:
        if (i in seen):
            seen[i]-=1
            if(seen[i]==-1):
                return False
    return True
    

           


print(isAnagram('tgzonrrftzq','tqzzrtnrftg'))