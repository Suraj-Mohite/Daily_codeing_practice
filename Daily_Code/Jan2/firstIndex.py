def firstIndex(arr,ind,num):
    if ind==len(arr):
        return
    if arr[ind]==num:
        return ind
    return firstIndex(arr,ind+1,num)


# print(firstIndex([10,20,30,40,20,20,60,20,6,6,3,20,50,6,89,7],0,20))

def lastIndex(arr,ind,num):
    if ind==len(arr):
        return 
    if arr[~ind]==num:
        return len(arr)+(~ind)
    return lastIndex(arr,ind+1,num)
    
# print(lastIndex([10,20,30,40,20,20,60,20,6,6,3,20,50,6,89,7],0,30))

#Another Approach if num not found return -1

def findLastIndex(arr,ind,num):
    if ind==len(arr):
        return -1
    lind=findLastIndex(arr,ind+1,num)
    if lind==-1:
        if arr[ind]==num:
            return ind
        else:
            return -1
    else:
        return lind

print(findLastIndex([10,20,30,40,20,20,60,20,6,6,3,20,50,6,89,7],0,200))