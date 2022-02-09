#you are given one pivet and array partition array where all numbers less than equal to pivet at left and rest at right

def partitionArray(arr,pivet,lo,hi):
    i,j=lo,lo
    while j<=hi:           #[8,5,2,2,1,4,9,3,7,2,65,2,1,33]
        if arr[i]<=pivet:
            i+=1
        elif arr[j]<=pivet:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    # print('partetian : ',i-1)
    return i-1

# def partitionArray(arr,pivet):
#     i,j=0,0
#     while j<len(arr):
#         if arr[j]>pivet:
#             j+=1
#         else:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#             j+=1


# arr=[8,5,2,2,1,4,9,3,7,2,65,2,1,33]    
# pivet=330
# partitionArray(arr,pivet,0,13)
# # print(arr)


def quickSort(arr,lo,hi):
    if lo>=hi:
        return

    pivet=arr[hi]
    pi=partitionArray(arr,pivet,lo,hi)
    quickSort(arr,lo,pi-1)
    quickSort(arr,pi+1,hi)

# arr=[8,5,2,1,33]    
# quickSort(arr,0,len(arr)-1)
# print(arr)



#Q: find kth minimum number in given array

def QuickSelect(arr,k,lo,hi):
    if k<=0 or k>len(arr):
        return "invalid k"
    pivet=arr[hi]
    pa=partitionArray(arr,pivet,lo,hi)

    if pa==k-1:
        return arr[pa]
    if pa>k-1:
        return QuickSelect(arr,k,lo,pa-1)
    else:
       return QuickSelect(arr,k,pa+1,hi)


arr=[8,5,2,1,33]
print(QuickSelect(arr,4,0,len(arr)-1))