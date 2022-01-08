# def targetSumSubset(arr,target,i=0,ans=[]):
#     if sum(ans)==target:
#         print(ans)
#         return
#     if i==len(arr):
#         return
#     ans.append(arr[i])
#     targetSumSubset(arr,target,i+1,ans)
#     ans.pop()
#     targetSumSubset(arr,target,i+1,ans)

def targetSumSubset(arr,target,i=0,ans=[],sum=0):
    if sum==target:
        print(ans)
        return
    if i==len(arr):
        return
    ans.append(arr[i])
    targetSumSubset(arr,target,i+1,ans,sum+arr[i])
    ans.pop()
    targetSumSubset(arr,target,i+1,ans,sum)

# targetSumSubset([60,10,20,30,40,50],60)
targetSumSubset([60,10,20,30,40,50],60,0,[],0)