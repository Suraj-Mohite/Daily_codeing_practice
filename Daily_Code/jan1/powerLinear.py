# accept x and n from user and return x^n using recursion

def powerLinear(x,n):
    if n==0:
        return 1
    return x*powerLinear(x,n-1)

# print(powerLinear(5,0))


#BETTER SOLUTION

def powerLinearbetter(x,n):
    if n==0:
        return 1
    if n%2==0:
        return powerLinearbetter(x,n//2)*powerLinearbetter(x,n//2)
    else:
        return x*powerLinearbetter(x,n//2)*powerLinearbetter(x,n//2)

# print(powerLinearbetter(5,3))
# print(powerLinearbetter(5,2))
# print(powerLinearbetter(5,0))


#BEST SOLUTION
def powerLinearBest(x,n):
    if n==0:
        return 1
    halfn=powerLinearBest(x,n//2)
    halfn=halfn*halfn
    if n%2==1:
        return x*halfn
    return halfn
print(powerLinearBest(5,4))
print(powerLinearBest(5,5))
print(powerLinearBest(5,0))

