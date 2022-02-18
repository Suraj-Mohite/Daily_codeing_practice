def peakInUnsorted(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if arr[mid+1]<arr[mid]:
            end=mid
        else:
            start=mid+1

    return arr[start]

print(peakInUnsorted([1,2,5,4,12,5,9,8]))
