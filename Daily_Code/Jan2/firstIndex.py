def firstIndex(arr,ind,num):
    if ind==len(arr):
        return
    if arr[ind]==num:
        return ind
    return firstIndex(arr,ind+1,num)


print(firstIndex([10,20,30,40,20,20,60,20,6,6,3,20,50,6,89,7],0,20))

def lastIndex(arr,ind,num):
    if ind==len(arr):
        return 
    if arr[~ind]==num:
        return len(arr)+(~ind)
    return lastIndex(arr,ind+1,num)
    
print(lastIndex([10,20,30,40,20,20,60,20,6,6,3,20,50,6,89,7],0,30))