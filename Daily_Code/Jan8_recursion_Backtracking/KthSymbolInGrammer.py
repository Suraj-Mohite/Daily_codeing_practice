"""
I/P :n=4,k=5 
o/p :1

explation 
n=1 0
n=2 0 1
n=3 0 1 1 0
n=4 0 1 1 0 (1) 0 0 1

video Aditya verma you tube 
"""

def KthSymbol(n,k):
    total=2**(n-1)
    if k>total:
        return "Invalid K"
    if n==1 and k==1:
        return 0
    mid=total//2
    if k<=mid:
        return KthSymbol(n-1,k)
    else:
        if KthSymbol(n-1,k-mid)==1:
            return 0
        return 1
print(KthSymbol(5,9))