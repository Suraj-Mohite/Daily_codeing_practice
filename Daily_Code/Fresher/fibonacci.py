# print first n fibonacci numbers
def fibonacci(num):
    first=0
    second=1
    print(first)

    for i in range(1,num):
        print(second)
        first,second=second,first+second

# fibonacci(3)

#print fibonacci numbers till N (excluding N)

def fibTillN(num):
    first=0
    second=1
    print(first)
    while second<num:
        print(second)
        first,second=second,first+second

# fibTillN(13)

#print fibonacci numbers till N (including N)

def fibTillNinclude(num):
    first=0
    second=1
    print(first)
    while second<=num:
        print(second)
        first,second=second,first+second

# fibTillNinclude(100)

#return nth fibonacci num
def fib(num):
    if num<=0:
        return "invalid"
    if num==1:
        return 0
    if num==2:
        return 1
    return fib(num-1)+fib(num-2)

# print(fib(5))

#print n fibonacci num using recursion
def nFib(num):
    def fib(num):
        if num<=0:
            return "invalid"
        if num==1:
            return 0
        if num==2:
            return 1
        return fib(num-1)+fib(num-2)
    for i in range(1,num+1):
        print(fib(i))

nFib(15)
    