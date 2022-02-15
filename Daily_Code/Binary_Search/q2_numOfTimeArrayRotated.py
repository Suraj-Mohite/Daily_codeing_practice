# find min in rotated array or how many times array is rotated all elements are unique

def numOfTimeRotated(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if arr[mid]<arr[end]:
            end=mid
        else:
            start=mid+1
    return start

# print(numOfTimeRotated([4,3]))


# find min in rotated array or how many times array is rotated Duplicates present

def numOfTimeRotatedDuplicate(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if arr[mid]<=arr[end]:
            end=mid
        else:
            start=mid+1
    return start

# print(numOfTimeRotatedDuplicate([7,7,7,4,4,5,5,5,6]))



#incomplete

# #find max in rotated sorted array NO Duplicate

def maxInRotatedSortedArray(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if arr[mid]>arr[start]:
            start=mid
        else:
            end=mid-1
    if start<len(arr)-1 and arr[start+1]>arr[start]:
        return start+1
    return start

print(maxInRotatedSortedArray([8,9,10,11,13,6]))
