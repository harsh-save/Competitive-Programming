from tkinter import NO


def gridChallenge(grid):
    res =[sorted(g) for g in grid]
    res_v=[list(x) for x in zip(*res)]
    res_v_s=[sorted(i) for i in res_v]

    if res == sorted(res) and res_v==res_v_s:
        return 'YES'
    else:
        return 'NO'

   
    
 






print(gridChallenge(['abc','aed','efg']))
