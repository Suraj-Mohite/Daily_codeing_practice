def SubsetSum(arr):
    res=[]
    def subsetInner(ind,sum):
        if ind==len(arr):
            res.append(sum)
            return
        subsetInner(ind+1,sum+arr[ind])
        subsetInner(ind+1,sum)
    subsetInner(0,0)

    res.sort()    
    return res

print(SubsetSum([1,6]))
