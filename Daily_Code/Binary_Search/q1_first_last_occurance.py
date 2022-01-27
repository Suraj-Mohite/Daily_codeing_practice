def firstAndLastOccurance(arr,num):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=start+((end-start)//2)
        if len(arr)==1 and arr[0]==num:
            print(0)
            break
        if arr[mid]==num and arr[mid-1]!=num:
            print(mid)
            break

        if (arr[mid]==num and arr[mid-1]==num) or arr[mid]>num:
            end=mid-1
        
        if arr[mid]<num:
            start=mid+1

firstAndLastOccurance([100],100)