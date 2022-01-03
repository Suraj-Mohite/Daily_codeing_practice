# Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Shift: 23
# Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

# Text : ATTACKATONCE
# Shift: 4
# Cipher: EXXEGOEXSRGI

# def CaesarCipher(text,n):
#     n%=26
#     result=""

#     for letter in text:
#         l1=ord(letter)
#         if letter.isupper():
#             l2=(l1+n)%90
            
#             if l2==0:
#                 l2=l1+n
#             if l2<65:
#                 l2+=64
#             result+=chr(l2)
#         elif letter.islower():
#             l2=(l1+n)%122
            
#             if l2==0:
#                 l2=l1+n
#             if l2<97:
#                 l2+=96
#             result+=chr(l2)
#         else:
#             result="Invalid Input"
#             break

#     return result

# print(CaesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ",23))
# print(CaesarCipher("ATTAC659NCE",4))
# print(CaesarCipher("ATTacKATOnce",4))


# def CaesarCipher(text,n):
#     result=""

#     for letter in text:
#         l1=ord(letter)
#         if letter.isupper():
#             l2=(l1+(n-65))%26+65
#             result+=chr(l2)
#         elif letter.islower():
#             l2=(l1+(n-97))%26+97
#             result+=chr(l2)
#         else:
#             result="Invalid Input"
#             break

#     return result

# print(CaesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ",23))
# print(CaesarCipher("ATTAC659NCE",4))
# print(CaesarCipher("A",66))



#remove all character except letters

# def removeCharExceptLetter(String):
#     result=""
#     for letter in String:
#         if letter.isupper() or letter.islower():
#             result+=letter
#     return result

# print(removeCharExceptLetter("hf7@*hhggdf^^dhsb+-3BF"))

#find maximum sum of subarray

# def maxSubarraySum(array):
#     total=0

#     for i in range(len(array)):
#         s=sum(array[i:])
#         if s > total:
#             total=s
#             array=array[i:]
#     return array,total

# print(maxSubarraySum([1,2,-4,3,4]))


# def reverseNum(num):
#     sum=0
#     while(num):
#         digit=num%10
#         sum=(sum*10)+digit
#         num//=10
#     return sum

# print(reverseNum(0))


# def frequencyOfChar(String):
#     d={}
#     for letter in String:
#         d[letter]=d.get(letter,0)+1
    
#     return d

# print(frequencyOfChar("suraj gggsssrrrprakash mohite"))

def frequencyOfChar(String,ch):
    freq=0
    for letter in String:
        if letter==ch:
            freq+=1
    
    return freq

print(frequencyOfChar("suraj gggsssrrrprakash mohite",'s'))