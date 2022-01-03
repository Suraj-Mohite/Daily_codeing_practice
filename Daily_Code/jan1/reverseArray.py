#reverse an array using recursion

def reverseArray(arr,n):
    if n==len(arr)//2:
        return arr
    arr[n],arr[~n]=arr[~n],arr[n]
    # arr[n],arr[len(arr)-n-1]=arr[len(arr)-n-1],arr[n]
    return reverseArray(arr,n+1)
    
print(reverseArray([5,4,1,8,6,3],0))