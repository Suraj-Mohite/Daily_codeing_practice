def combinationSum(arr,i,sum,ds):
    if i==len(arr):
        if sum==0:
            print(ds)
        return

    if arr[i]<=sum:
        ds.append(arr[i])
        combinationSum(arr,i,sum-arr[i],ds)
        ds.remove(arr[i])
    combinationSum(arr,i+1,sum,ds)

combinationSum([2,3,6,7],0,7,[])