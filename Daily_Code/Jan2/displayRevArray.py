def displayRevArray(arr,ind):
    if ind==len(arr):
        return
    displayRevArray(arr,ind+1)
    print(arr[ind])

displayRevArray([10,20,30,40,50],0)