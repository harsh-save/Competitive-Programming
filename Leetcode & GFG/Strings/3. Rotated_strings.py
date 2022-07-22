def areRotations(s1,s2):

       #code here
    for i in range(len(s1)):
        s1=s1[1:len(s1)]+s1[0]
        if(s1==s2):
            return True
    return False
    
    




print(areRotations('geeksforgeeks','forgeeksgeeks'))