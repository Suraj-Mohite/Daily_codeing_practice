#lower bound means first_num_occur >= target else retun size of array
#upper bound means first_num_occur > target


def lowerBound(arr,target):
    n=len(arr)
    start=0
    end=n-1
    # ans=n     #using ans variable
    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]>=target:
            # ans=arr[mid]
            end=mid-1
        else:
            start=mid+1
    
    if start<0 or start>=n or arr[start]<target:
        return n
    return start


def upperBound(arr,target):
    n=len(arr)
    start=0
    end=n-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    if start<0 or start >=n or arr[start]<=target:
        return n
    return start

# print(lowerBound([1,1,3,5,7,9,9,9,9,9,11],10))
# print(upperBound([1,1,3,5,7,9,9,9,9,9,11],10))

#find frequency of number using upper and lower bound
def findFreqOfNum(arr,target):
    lower=lowerBound(arr,target)
    upper=upperBound(arr,target)

    if upper==lower:
        return 0
    return upper-lower

print(findFreqOfNum([1,1,3,5,7,9,9,9,9,9,11],11))