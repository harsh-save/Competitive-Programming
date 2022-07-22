from operator import le


def minimumBribes(q):
    bribes=[0]*len(q)
    for i in range(len(q)):
        for j in range(i+1,len(q)):
            if q[i]>q[j]:
                bribes[i] +=1
    if max(bribes)>=3:
        print('Too chaotic')
    else:
        return sum(bribes)


print(minimumBribes([2, 1, 5, 3, 4]))