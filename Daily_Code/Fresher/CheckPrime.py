def isPrime(num):
    if num==1:
        return False
    for i in range(2,int(num**(0.5))+1):
        if num%i==0:
            return False
    return True

# print(isPrime(107))

#find prime numbers in given range
def findPrime(start,end):
    for i in range(start,end+1):
        if isPrime(i):
            print(i)

# findPrime(2,47)

# find N prime Numbers

def nPrimeNum(n):
    num=2
    while n>0:
        if isPrime(num):
            print(num)
            n-=1
        num+=1
nPrimeNum(11)
        