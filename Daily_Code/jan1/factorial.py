#find n! using recursion

def fact(n):
    if n<0:
        return 'Invalid Input'
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

#factorial using recursion in one line
def fact1(n):
    return "Invalid Input" if n<0 else 1 if n==0 or n==1 else n*fact1(n-1)

print(fact1(5))
print(fact1(0))
print(fact1(-3))