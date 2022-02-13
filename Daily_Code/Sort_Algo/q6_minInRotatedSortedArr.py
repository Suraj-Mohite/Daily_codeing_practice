def minInRotatedSortedArr(arr):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=arr[start]+arr[end]//2

        if mid>=1 and mid<len(arr)-1 and arr[mid-1]>arr[mid] and arr[mid+1]>arr[mid]:
            return arr[mid]
        if mid>=1:
            if arr[mid-1]<arr[mid]:
                end=mid-1
            else:
                start=mid+1

print(minInRotatedSortedArr([11,12,15,18,2,3,6,7,8,10]))
        