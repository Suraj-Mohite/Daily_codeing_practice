def chkPalindrome(String,ind=0):
    if len(String)==0:
        return 'Invalid Input'
    if ind==len(String)//2:
        return True
    if String[ind]!=String[~ind]:
        return False
    return chkPalindrome(String,ind+1)

print(chkPalindrome('nitin'))
print(chkPalindrome('n'))
print(chkPalindrome('ni'))
print(chkPalindrome('nn'))
print(chkPalindrome(''))
