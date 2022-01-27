def isArmstrong(num):
    temp=num
    sum=0
    while num>0:
        digit=num%10
        sum+=digit**3
        num//=10
    if temp==sum:
        return True
    return False

# print(isArmstrong(1))


def findArmstrong(start,end):
    for i in range(start,end+1):
        if isArmstrong(i):
            print(i)

# findArmstrong(0,500)

#find 0 to n armstrong
def nArmstrong(n):
    num=0
    while n>0:
        if isArmstrong(num):
            print(num)
            n-=1
        num+=1

nArmstrong(6)