from operator import le


def isPallindrome(S):
    S=list(S)
    rightpointer=len(S)-1
    for i in range(len(S)):
        if(S[i]!=S[rightpointer] and i<=rightpointer):
            return False
        rightpointer-=1
    return True

print(isPallindrome('abc'))



