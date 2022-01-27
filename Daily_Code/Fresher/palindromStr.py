#using split operator
def isPalindrome(String):
    String=String.lower()
    if String==String[::-1]:
        return True
    return False

# print(isPalindrome("NiTIn"))

def isPalindrome1(String):
    n=len(String)
    for i in range(n//2):
        if String[i]!=String[n-i-1]:
            return False
    return True

# print(isPalindrome1("NitiN"))

def isPalindrome2(String):
    n=len(String)
    i=0
    while i<n//2:
        if String[i]!=String[n-i-1]:
            return False
        i+=1

    return True
        

# print(isPalindrome2("nnnn"))

#using Recursion
def pal(String,i=0):
    n=len(String)
    if i==n//2:
        return True
    if String[i]!=String[n-i-1]:
        return False
    return pal(String,i+1)

# print(pal("nitin"))

def palindrome0(String):
    if String=="".join(reversed(String)):
        return True
    return False

print(palindrome0("nitn"))
