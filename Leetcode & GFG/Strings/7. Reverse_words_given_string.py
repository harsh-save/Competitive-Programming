def reverseWords(S):
    S=S.split('.')
    return '.'.join(S[::-1])


print(reverseWords('i.like.this.program.very.much'))