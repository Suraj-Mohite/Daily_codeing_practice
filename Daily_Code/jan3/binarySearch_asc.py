def binarySearchAsc(arr,num):
    first=0
    last=len(arr)-1

    while(first<=last):
        if arr[first]==num:
            return first
        if arr[last]==num:
            return last

        mid=first+(last-first)//2  #instead of first+last//2 i used this to avoid int overflow

        if arr[mid]==num:
            return mid
        if num>arr[mid]:
            first=mid+1
        else:
            last=mid-1

print(binarySearchAsc([10,20,30,40,50,60,70,80,90,100],80))
