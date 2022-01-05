#you have given sorted array and target. return index of numbers whose sum is target

def targetSum2(arr,target):
    p=0
    q=len(arr)-1

    while(p<q):
        num=arr[p]+arr[q]
        if num==target:
            return [p,q]
        if num<target:
            p+=1
        else:
            q-=1
    return 'no pair of number'

print(targetSum2([1,2,3,4,6,8,9],14))
        
