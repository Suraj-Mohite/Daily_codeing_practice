def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[10,9,8,7,6,5,4,3,2,1]
bubbleSort(arr)
print(arr)