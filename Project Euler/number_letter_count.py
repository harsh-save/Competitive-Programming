"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
def number_letters(n):

    nums2words={
        1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
        14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
        70:'seventy',80:'eighty',90:'ninety',100:'hundred',200:'two hundred',300:'three hundred',400:'four hundred',500:'five hundred',600:'six hundred',
        700:'seven hundred',800:'eight hundred',900:'eight hundred',1000:'thousand'
    }
    count=0
    
    for i in range(1,n):
        if i==1000:
            count+=len("onethousand")
        elif i<=20:
            count+=len(nums2words[i])
        
        elif len(str(i))==2:
            if i in nums2words:
                count+=len(nums2words[i])
            else:
                count+=len(nums2words[i-i%10]+nums2words[i%10])
        else:
            if i in nums2words:
                count+=len(nums2words[i])
            else:
                print(i)
                count+=len(nums2words[i-i%100]+'and'+nums2words[(i%100)-(i%10)]+nums2words[i%10].lower())
            #count+=len(temp)



    print(count)


    #res=nums2words[n-n%100]+'and'+nums2words[(n%100)-(n%10)]+nums2words[n%10].lower()
    #print(res)

number_letters(1000)


