#find integer square root of N example sq root of 26=5

def squareRoot(num):
    if num<0:
        num=-num

    start=1
    end=num//2
    if end==0:
        return 1

    while start<=end:
        mid=(start+end)//2

        # if mid*mid<=num:
        if mid**2<=num:
            start=mid+1
        else:
            end=mid-1

    return end

def cubeRoot(num):
    if num<0:
        num=-num

    start=1
    end=num

    while start<=end:
        mid=(start+end)//2

        # if mid*mid*mid<=num:
        if mid**3<=num:
            start=mid+1
        else:
            end=mid-1

    return end

print(squareRoot(1))
# print(cubeRoot(80))