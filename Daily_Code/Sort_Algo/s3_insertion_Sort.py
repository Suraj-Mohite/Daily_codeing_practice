def insertionSort(arr):
    n=len(arr)
    for i in range(n-1):
        j=i+1
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        print(arr)

arr=[2,9,5,1,3]
insertionSort(arr)
print(arr)