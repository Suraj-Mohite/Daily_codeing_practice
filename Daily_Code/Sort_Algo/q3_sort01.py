def sort01(arr):
    i,j=0,0

    while j<len(arr):
        if arr[i]==0:
            i+=1
        elif arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    
arr=[1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0]
sort01(arr)
print(arr)
        
