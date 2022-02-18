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
    return arr[start]

# print(numOfTimeRotated([4,3]))


# find min in rotated array or how many times array is rotated Duplicates present

def numOfTimeRotatedDuplicate(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if arr[mid]<arr[end]:
            end=mid
        elif arr[mid]>arr[end]:
            start=mid+1
        else:
            end-=1
    return arr[start]

print(numOfTimeRotatedDuplicate([1,1,1,0,0,1]))



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
        return arr[start+1]
    return arr[start]

# print(maxInRotatedSortedArray([8,9,10,11,12,13]))

# #find max in rotated sorted array  Duplicate

def maxInRotatedSortedArray(arr):
    start=0
    end=len(arr)-1

    while start<end:
        mid=start+(end-start)//2

        if mid!=start and arr[mid]>=arr[start]:
            start=mid
        else:
            end=mid-1
    if start<len(arr)-1 and arr[start+1]>=arr[start]:
        return arr[start+1]
    return arr[start]

# print(maxInRotatedSortedArray([1,0,1,1,1,1]))
# print(maxInRotatedSortedArray([5,5,5,5,5,5]))
