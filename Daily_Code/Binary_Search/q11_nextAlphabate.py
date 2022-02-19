#find next alphabate of target from given arr

def nextAlphabate(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2

        # if arr[mid]>target:
        if arr[mid].lower()>target.lower():     #if we want case insensitive 
            end=mid-1
        else:
            start=mid+1

    if start<0 or start>len(arr)-1:
        return -1
    return arr[start]

print(nextAlphabate(['a','b','c','d','f','H'],'f'))

