def numOfTimeSorted(arr):
    start=0
    end=len(arr)-1

    mid=start+((end-start)//2)

    while start<=end:
        if arr[mid-1]>arr[mid]:
            return