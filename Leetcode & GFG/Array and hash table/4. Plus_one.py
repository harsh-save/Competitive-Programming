def plusOne(digits):
    if(digits[len(digits)-1]+1<10):
        digits[len(digits)-1]=digits[len(digits)-1]+1
        return digits
    
    else:
        return list(str(int("".join(str(i) for i in digits)) + 1))
        




print(plusOne([1,2,9]))