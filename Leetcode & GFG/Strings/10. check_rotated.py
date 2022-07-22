def isRotated(s1,s2):
    s1=s1[2:]+s1[:2]
    if(s1==s2):return True

    return False

print(isRotated('geeksforgeeks','geeksgeeksfor'))