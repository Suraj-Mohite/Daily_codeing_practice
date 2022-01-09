#return first subset whoes sum is k

def first_subsetofSumK(arr,i,ans,sum,target):
    if i==len(arr):
        if sum==target:
            print(ans)
            return True
        return False
    ans.append(arr[i])
    if first_subsetofSumK(arr,i+1,ans,sum+arr[i],target):
        return True
    ans.remove(arr[i])
    if first_subsetofSumK(arr,i+1,ans,sum,target):
        return True
    return False

first_subsetofSumK([1,2,3,4],0,[],0,6)