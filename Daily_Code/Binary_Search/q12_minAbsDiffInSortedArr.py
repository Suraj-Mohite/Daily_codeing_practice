# return the number from array which will give minimum abs difference if we sustract it from target value

def minAbsDiffInSortedArr(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]==target:
            return arr[mid]
        if arr[mid]<target:
            start=mid+1
        else:
            end=mid-1

    #below code will handle condition when there is only one element in array
    if start<0 or start>=len(arr):
        return arr[end]

    if end<0 or end>=len(arr):
        return arr[start]
    
    no1=abs(arr[start]-target)
    no2=abs(arr[end]-target)
    
    if no1<no2:
        return arr[start]
    else:
        return arr[end]

print(minAbsDiffInSortedArr([10,11],11))