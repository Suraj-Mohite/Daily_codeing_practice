#find frequency of number in sorted array O(logn)

#find First occurance with ans variable
# def findFirstOccur(arr,target):
#     start=0
#     end=len(arr)-1
#     ans=-1
#     while start<=end:
#         mid=start+(end-start)//2

#         if arr[mid]>=target:
#             ans=mid
#             end=mid-1
#         else:
#             start=mid+1
#     return ans

# print(findFirstOccur([1,3,5,6,6,6,6,6,7,8,8,9],90))

#find First occurance without ans variable
def findFirstOccur(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    if start < 0 or start >=len(arr) or arr[start]!=target:
        return -1
    return start

# print(findFirstOccur([1,3,5,6,6,6,6,6,7,8,8,9],-16))

#find last Occurance 
def lastOccur(arr,target):
    start=0
    end=len(arr)-1
    # ans=-1 #using ans variable
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]<=target:
            # ans=mid
            start=mid+1
        else:
            end=mid-1
    if end<0 or end>=len(arr) or arr[end]!=target:
        return -1
    return end
    # return ans

# print(lastOccur([1,3,5,6,6,6,6,6,7,8,8,9],-16))

def findFreqOfNum(arr,target):
    f=findFirstOccur(arr,target)
    if f==-1:
        return "Target Does Not Exist"
    l=lastOccur(arr,target)
    return (l-f)+1

print(findFreqOfNum([1,1,1,3,5,6,6,6,6,6,7,8,8,9],1))
        
        
