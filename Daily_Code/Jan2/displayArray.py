def displayArray(arr,ind):
    if ind==len(arr):
        return 
    print(arr[ind])
    displayArray(arr,ind+1)

displayArray([10,20,30,40,50,60],0)