#bitonic array means array is continuously increasing upto some point and then decreasing 

def maxInBitonic(arr):
    start=0
    end=len(arr)-1

    while(start<end):
        mid=start+(end-start)//2

        if arr[mid+1]<arr[mid]:
            end=mid
        else:
            start=mid+1
    return arr[start]

print(maxInBitonic([1,2]))
