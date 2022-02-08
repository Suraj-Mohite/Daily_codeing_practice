def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

# arr=[7,5,1,9,6,3,4,88,7,2]
arr=[2,1]
selectionSort(arr)
print(arr)
