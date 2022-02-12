#1 find min and max
#2 make array of that size (min-max)
#3 index 0 will represent min and last index will represent max
#4 make prefix array
#5 substract each element of array by 1
#6 itarate original array reverse and by crating new array put that value in it substract elements of subtracted prifix array by one

def countSort(arr):
    minValue=min(arr)
    maxValue=max(arr)
    new_arr=[0]*((maxValue-minValue)+1)
    for i in arr:
        new_arr[i-minValue]+=1

    # pre=0
    # prefix=[]
    # for i in new_arr:
    #     prefix.append(i+pre-1)
    #     pre+=i
    
    pre=0
    for i in range(len(new_arr)):
        temp=new_arr[i]
        new_arr[i]+=pre-1
        pre+=temp
        

    n=len(arr)
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ans[new_arr[arr[i]-minValue]]=arr[i]
        new_arr[arr[i]-minValue]-=1

    # n=len(arr)
    # ans=[0]*n
    # for i in range(n-1,-1,-1):
    #     ans[prefix[arr[i]-minValue]]=arr[i]
    #     prefix[arr[i]-minValue]-=1

    # return(ans)
    return(ans)

print(countSort([2,2,3,4,5,6,2,3,3,8,1,9,9,9,9,6,6,9]))