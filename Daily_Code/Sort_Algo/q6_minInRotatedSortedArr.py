def minInRotatedSortedArr(arr):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=arr[start]+arr[end]//2

        if mid>0 and mid<len(arr)-1 and arr[mid-1]>arr[mid] and arr[mid+1]>arr[mid]:
            return mid
        if mid>0 and 
        