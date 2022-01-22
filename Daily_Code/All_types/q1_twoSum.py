# find x,y whose sum is target

def twoSum(arr,target):
    map={}
    ans=[]
    for i,n in enumerate(arr):
        diff=target-n
        if diff in map:
            ans.append([diff,n])
        else:
            map[n]=i
    return ans

# print(twoSum([5,6,4,2,3,9,7,8],16))


#find x,y in array where x=y/2.
#My APPROACH
def getXandY(arr):
    map={}
    ans=[]
    arr.sort(reverse=True)
    for i,n in enumerate(arr):
        y=2*n
        if y in map:
            ans.append([n,y])
        map[n]=i
    return ans

# print(getXandY([5,6,4,2,3,9,7,8]))

#BEST APPROACH

def getXandY(arr):
    set1=set()
    ans=[]
    for i in arr:
        set1.add(2*i)
    for i in arr:
        if i in set1:
            ans.append([i,i//2])
    return ans
print(getXandY([5,6,4,2,3,9,7,8]))

#find x,y in array where x=y/2.

# def getXandY(arr):
#     map={}
#     ans=[]
#     arr.sort(reverse=True)
#     for i,n in enumerate(arr):
#         y=2*n
#         if y in map:
#             ans.append([y,n])
#         map[n]=i
#     return ans

# print(getXandY([5,6,4,2,3,9,7,8]))