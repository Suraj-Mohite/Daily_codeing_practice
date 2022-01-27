def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

# print(factorial(5))

def fact(num):
    temp=num
    sum=0
    while num>0:
        digit=num%10
        sum+=factorial(digit)
        num//=10
    
    if temp==sum:
        return True
    return False

print(fact(145))