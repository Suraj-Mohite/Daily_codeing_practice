def searchInRotatedSortedArr(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        if arr[start]<=arr[mid]:
            if target>=arr[start] and target<=arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if target>=arr[mid+1] and target<=arr[end]:
                start=mid+1
            else:
                end=mid-1
    return -1

print(searchInRotatedSortedArr([7,8,9,1,2,3,4,5],15))