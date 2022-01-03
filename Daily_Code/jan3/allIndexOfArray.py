#find all indices of the entered number in an array

def allIndex(arr,ind,num,fsf):
    if ind==len(arr):
        return [0]*fsf
    if arr[ind]==num:
        ans=allIndex(arr,ind+1,num,fsf+1)
        ans[fsf]=ind
        return ans
    else:
        return allIndex(arr,ind+1,num,fsf)

print(allIndex([10,20,50,1,0,30,2,1,10,6,4,10,9,10,10,5],0,6,0))
