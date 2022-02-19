def SearchInNearlySortedArr(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]==target:
            return mid
        if (mid-1)>=start and arr[mid-1]==target:
            return mid-1
        if (mid+1)<=end and arr[mid+1]==target:
            return mid+1
        
        if arr[mid]>target:
            end=mid-2
        else:
            start=mid+2
    return -1

# print(SearchInNearlySortedArr([5,10,30,20,40,50],20))
print(SearchInNearlySortedArr([5,10,20,40,50],20))