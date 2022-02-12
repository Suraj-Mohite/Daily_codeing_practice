def countSort(arr,exp):
    
    new_arr=[0]*10
    for i in range(len(arr)):
        new_arr[(arr[i]//exp)%10]+=1

    pre=0
    for i in range(len(new_arr)):
        temp=new_arr[i]
        new_arr[i]+=pre-1
        pre+=temp
        

    n=len(arr)
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ind=(arr[i]//exp)%10
        ans[new_arr[ind]]=arr[i]
        new_arr[ind]-=1

    return(ans)


def redixSort(arr):
    maxValue=max(arr)

    exp=1
    ans=[]
    while exp<=maxValue:
        ans=countSort(arr,exp)
        exp*=10
    return ans

# arr=[232,349,721,26,29,423]
# print(redixSort(arr))


def countSortDate(arr,exp,mod,daterange):
    
    new_arr=[0]*daterange
    for i in range(len(arr)):
        new_arr[(arr[i]//exp)%mod]+=1

    pre=0
    for i in range(len(new_arr)):
        temp=new_arr[i]
        new_arr[i]+=pre-1
        pre+=temp
        

    n=len(arr)
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ind=(arr[i]//exp)%mod
        ans[new_arr[ind]]=arr[i]
        new_arr[ind]-=1

    return(ans)

def sortDate(arr):
    ans=[]
    ans=countSortDate(arr,1000000,100,32) #days max days is 31 in month
    ans=countSortDate(ans,10000,100,13) # month max month is 12
    ans=countSortDate(ans,1,10000,2501) #year max year is 2500 given
    return ans

print(sortDate([12041996,20101996,5071997,12041989,11081987,12011997]))