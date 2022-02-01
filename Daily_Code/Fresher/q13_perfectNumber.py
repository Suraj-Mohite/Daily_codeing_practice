#Write a program to print Perfect number from 1 to 10000

def is_perfectNumber(num):
    sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum+=i
    
    if sum==num:
        return True
    return False

def findPerfectNum(n):
    for i in range(1,n+1):
        if is_perfectNumber(i):
            print(i)

findPerfectNum(10000)