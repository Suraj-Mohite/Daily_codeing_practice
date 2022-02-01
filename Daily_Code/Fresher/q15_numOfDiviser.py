#Write a Python program to find the number of divisors of a given integer is even or odd.

def countEvenOddDiviser(num):
    if num<=0:
        return 0
    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
    print(cnt)
    if cnt%2==0:
        return 'Even'
    return 'Odd'

print(countEvenOddDiviser(10))