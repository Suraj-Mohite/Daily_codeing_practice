# def mainFun(arr,target):
    # ds=[]
    # arr.sort()
    # ans=[]
    # def combinationSum2(ind,target,ds):
    #     if target==0:
    #         ans.append(ds.copy())
    #         return
    #     num=None
    #     for i in range(ind,len(arr)):
    #         if arr[i]>target:
    #             break
    #         if arr[i]!=num:
    #             ds.append(arr[i])
    #             num=arr[i]
    #             combinationSum2(i+1,target-arr[i],ds)
    #             ds.remove(arr[i])
    # combinationSum2(0,target,ds)
    # return ans

# print(mainFun([10,1,2,7,6,1,5],8))


