#floor means greatest element in array <= target

def floorInSortedArr(arr,target):
    start=0
    end=len(arr)-1
    ans=-1
    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]<=target:
            ans=mid
            start=mid+1
        else:
            end=mid-1
    
    return ans

# print(floorInSortedArr([4,5,6,7,8,9],15))

def floorInSortedArr1(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid-1
    if end<0 or end >len(arr)-1:
        return -1
    return end

print(floorInSortedArr1([40],15))