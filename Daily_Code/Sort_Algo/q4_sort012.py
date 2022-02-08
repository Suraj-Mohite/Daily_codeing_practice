def sort012(arr):
    i,j,k=0,0,len(arr)-1

    while j<k:
        # if arr[i]==0:
        #     i+=1
        #     j+=1
        # if arr[k]==2:
        #     k-=1
        if arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        if arr[j]==2:
            arr[j],arr[k]=arr[k],arr[j]
            k-=1
        if arr[j]==1:
            j+=1
# arr=[2,2,1,0,2,1,0,0,1,0,2,0,2,2,1,0,2,1,1,2]
arr=[2,2,2,2,1,1,1,1,0,0,0,0]
sort012(arr)
print(arr)