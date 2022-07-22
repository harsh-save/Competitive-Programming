def caesarCipher(s, k):
    
    encrypted_s=''
    for i in range(len(s)):
        if str(s[i]).isalpha()==False:
            encrypted_s+=s[i]
        else:
            if s[i].islower():
                encrypted_s+=chr(ord('a')+(ord(s[i])-ord('a')+k)%26)
            elif s[i].isupper():
                encrypted_s+=chr(ord('A')+(ord(s[i])-ord('A')+k)%26)

    return encrypted_s
       

       


print(caesarCipher('Hello_World!',4))