def SecondMax(arr):
    if len(arr)==0:
        return "invalid Input"
    m=max(arr)
    sec=min(arr)
    for i in arr:
        if i<m and i>sec:
            sec=i
    return sec

# print(SecondMax([9,9,8,7,5,4,12,12,6]))

def secMax(arr):
    if arr[0]>arr[1]:
        first=arr[0]
        second=arr[1]
    else:
        first=arr[1]
        second=arr[0]

    for i in range(2,len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]
    return second

print(secMax([5,6,4,7,9,8,55,55,6,4,22,22,1]))