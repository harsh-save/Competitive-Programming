def areIsomorphic(str1,str2):
    str1ht={}
    str2ht={}

    if(len(str1)!=len(str2)):
        return False
    
    for i in range(len(str1)):
        char1=str1[i]
        char2=str2[i]
        if(char1 not in str1ht):
            str1ht[char1]=char2
        if(char2 not in str2ht):
            str2ht[char2]=char1

        if(str1ht[char1]!=char2 or str2ht[char2]!=char1):
            return False
    return True

print(areIsomorphic('aab','xyz'))