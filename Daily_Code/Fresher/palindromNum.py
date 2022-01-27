def palindromeNumber(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=(rev*10)+digit
        temp//=10
    if rev==num:
        return True
    return False

print(palindromeNumber(545))