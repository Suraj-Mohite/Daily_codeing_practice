#ceil means smallest element of arr >=target

def ceilInSortedArr(arr,target):
    n=len(arr)
    start=0
    end=n-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    if start<0 or start>n-1:
        return -1
    return start

print(ceilInSortedArr([1,5,6,9,10,15],10))