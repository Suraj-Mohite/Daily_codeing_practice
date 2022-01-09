def subsetOfSumK(arr,i,ans,sum,target):
    if i==len(arr):
        if sum==target:
            print(ans)
        return
    ans.append(arr[i])
    subsetOfSumK(arr,i+1,ans,sum+arr[i],target)
    ans.remove(arr[i])
    subsetOfSumK(arr,i+1,ans,sum,target)

# subsetOfSumK([1,2,3,4],0,[],0,6)


#count the subsequences where sum is k

def countSubsetOfSumK(arr,i,sum,target):
    if i==len(arr):
        if sum==target:
            return 1
        return 0
    l=countSubsetOfSumK(arr,i+1,sum+arr[i],target)
    r=countSubsetOfSumK(arr,i+1,sum,target)
    return l+r

print(countSubsetOfSumK([1,2,3,4],0,0,9))