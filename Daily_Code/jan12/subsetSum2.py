def subsetSum2(arr):
    res=set()
    ans=[]
    def inner(ind):
        if ind==len(arr):
            t=tuple(ans)
            res.add(t)
            return
        ans.append(arr[ind])
        inner(ind+1)
        ans.pop()
        inner(ind+1)
    inner(0)
    return list(res)
print(subsetSum2([1,2,2]))