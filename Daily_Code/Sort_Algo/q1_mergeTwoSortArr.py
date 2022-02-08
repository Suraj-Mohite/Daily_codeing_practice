def mergeTwoSortedArray(arr1,arr2):
    i=0 
    j=0
    ans=[]
    n=len(arr1)
    m=len(arr2)

    while i<n or j<m:
        if i>=n:
            ans.extend(arr2[j:])
            break
        if j>=m:
            ans.extend(arr1[i:])
            break
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    return ans

# arr2=[1,3,5,7]
# arr1=[]
# print(mergeTwoSortedArray(arr1,arr2))


def mergeSort(arr):
    n=len(arr)
    if n==1:
        return arr

    mid=n//2
    arr1=mergeSort(arr[:mid])
    arr2=mergeSort(arr[mid:])
    return mergeTwoSortedArray(arr1,arr2)

print(mergeSort([7,4,1,3,6,8]))

