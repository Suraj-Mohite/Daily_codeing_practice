def targetSum(arr,target):
    arr.sort()
    i,j=0,len(arr)-1

    while(i<j):
        if arr[i]+arr[j]>target:
            j-=1
        elif arr[i]+arr[j]<target:
            i+=1
        else:
            print(arr[i],arr[j])
            i+=1
            j-=1

targetSum([7,15,3,18,6,4,19,2,12,11,9],15)