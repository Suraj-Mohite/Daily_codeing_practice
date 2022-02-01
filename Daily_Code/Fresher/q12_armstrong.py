#Write a program to print Armstrong number from 1 to 10000

def isArmstrong(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    
    if sum==num:
        return True
    return False

def findArmstrong(n):
    for i in range(1,n+1):
        if isArmstrong(i):
            print(i)

findArmstrong(10000)