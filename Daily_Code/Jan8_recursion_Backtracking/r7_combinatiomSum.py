#printcombination sum
def combinationSum(num,i,sum,ds):
    if i==len(num):
        if sum==0:
            print(ds)
        return

    if num[i]<=sum:
        ds.append(num[i])
        combinationSum(num,i,sum-num[i],ds)
        ds.remove(num[i])
    combinationSum(num,i+1,sum,ds)

# combinationSum([2,3,6,7],0,7,[])

#get combination sum
#APPROACH 1
def mainFunc(candidates,target):
    res=[]
    def inner(num,target,ans):
        if target==0:
            res.append(ans.copy())
            return
        for i in range(len(num)):
            if num[i]<=target:
                inner(num[i:],target-num[i],ans+[num[i]])
    inner(candidates,target,[])
    return res
print(mainFunc([2,3,6,7],7))

#APPROACH 2
def mainFunc1(arr,target):
    res=[]
    ans=[]
    def inner(ind,target):
        if ind==len(arr):
            if target==0:
                res.append(ans.copy())
            return

        if arr[ind]<=target:
            ans.append(arr[ind])
            inner(ind,target-arr[ind])
            ans.pop()
        inner(ind+1,target)
    inner(0,target)
    return res
print(mainFunc1([2,3,6,7],7))

