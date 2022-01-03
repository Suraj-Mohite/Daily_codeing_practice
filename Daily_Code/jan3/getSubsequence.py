def getSubSequence(String):
    if len(String)==0:
        return [""]
    arr=getSubSequence(String[1:])
    temp=[]

    for i in arr:
        temp.append(String[0]+i)
    return arr+temp

print(getSubSequence('abc'))


def getSubsequenceArray(arr,ind):
    if ind==len(arr):
        return [[]]
    temp=[]
    resArray=getSubsequenceArray(arr,ind+1)

    for i in resArray:
        temp.append([arr[ind]]+i)
    return resArray+temp

print(getSubsequenceArray([10,20,30],0))