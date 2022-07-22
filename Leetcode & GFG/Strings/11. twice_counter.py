def countWords(List, n):
    ht={}
    for i in List:
        if(i not in ht):
            ht[i]=1
        else:
            ht[i]+=1
    count=0
    for key,value in ht.items():
        if(value==2):
            count+=1
    return count

print(countWords(['Tom', 'Jerry', 'Thomas', 'Tom', 'Jerry', 'Courage', 'Tom', 'Courage'],8))