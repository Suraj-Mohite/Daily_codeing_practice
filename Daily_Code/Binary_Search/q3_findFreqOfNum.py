#find frequency of number in sorted array O(logn)

def findFreqOfNum(arr,target):
    start=0
    end=len(arr)-1
    cnt=0
    while start<=end:
        if arr[start]==target :
            cnt+=1
            
        if arr[end]==target:
            cnt+=1

        start+=1
        end-=1
    return cnt

print()
        
        
