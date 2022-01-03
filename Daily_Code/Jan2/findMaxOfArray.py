def maxOfArray(arr,ind):
    if ind==len(arr)-1:
        return arr[ind]
    return max(arr[ind],maxOfArray(arr,ind+1))

print(maxOfArray([1190,240,30,140,50],0))