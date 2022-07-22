def singleNumber(array):
    hashtable={}
    for i in array:
        if i not in hashtable:
            hashtable[i] =1
        else:
            hashtable[i]+=1
    
    for key,value in hashtable.items():
        if value==1:
            return key
    
   
    #print(hashtable)
print(singleNumber([1]))