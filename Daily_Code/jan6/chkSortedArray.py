def chkSortedArray(arr,ind):
    if ind==len(arr)-1:
        return True
    return arr[ind]<arr[ind+1] and chkSortedArray(arr,ind+1)

print(chkSortedArray([1,2,3,45,6,8,9],0))