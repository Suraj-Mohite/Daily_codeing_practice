def countTriplet(arr,i,ans,r):
    if len(ans)==3:
        print(ans)
        return 1
    if i==len(arr):
        return 0
    a=0
    b=0
    if len(ans)==0 or arr[i]//ans[-1]==r:
        ans.append(arr[i])
        a=countTriplet(arr,i+1,ans,r)
        ans.pop()
    b=countTriplet(arr,i+1,ans,r)
    return a+b

print(countTriplet([1,2,2,4],0,[],2))