#print N to 1 using recursion

def printNTo1(n):
    if n==0:
        return
    print(n,end=" ")
    printNTo1(n-1)

# printNTo1(5)

# printpattern using recursion
"""
* * * * *  
* * * *
* * *
* *
*

"""
def printNTo1Pat(n):
    if n==0:
        return
    print('* '*n)
    printNTo1Pat(n-1)

# printNTo1Pat(5)

def print1ToN(n):
    if n==0:
        return n
    print1ToN(n-1)
    print(n,end=" ")

# print1ToN(5)

#print Pattern 
"""
*
* *
* * *
* * * *
* * * * * 
"""
def Pattern(n):
    if n==0:
        return
    Pattern(n-1)
    print('* '*n)
# Pattern(5)

def printDecrisingIncrising(n):
    if n==0:
        return
    print(n)
    printDecrisingIncrising(n-1)
    print(n)

printDecrisingIncrising(5)