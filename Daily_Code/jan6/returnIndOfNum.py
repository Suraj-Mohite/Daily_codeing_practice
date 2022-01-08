def returnIndOfNum(arr,ind,target):
    if ind==len(arr):
        return []
    if arr[ind]==target:
        return [ind]+returnIndOfNum(arr,ind+1,target)
    else:
        return returnIndOfNum(arr,ind+1,target)


print(returnIndOfNum([10,20,1,0,30,30,60,10,10,10],0,10))