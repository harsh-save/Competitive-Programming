def NumberofElementsInIntersection(a,b,n,m):
    seen={}
    count=0
    x=[]
    y=[]
    if(n<m):
        x=b.copy()
        y=a.copy()
    else:
        x=a.copy()
        y=b.copy()
    for i in range(len(y)):
        if(y[i] not in seen):
            seen[y[i]]=y[i]
    for i in x:
        if(i in seen):
            count+=1
    print(count)

NumberofElementsInIntersection([3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6],5,6)

