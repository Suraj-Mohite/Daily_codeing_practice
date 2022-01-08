def is_safe(arr,i,j):
    res=True
    if i-1>=0 and arr[i-1][j]==1:
        res=False
    if i-1>=0 and j-1>=0 and arr[i-1][j-1]==1:
        res=False
    if i-1>=0 and j+1<len(arr[0]) and arr[i-1][j+1]==1:
        res=False
    return res


def NQueen(arr,i,ans):
    if i==len(arr):
        print(ans+".")
        return
    for col in range(len(arr[i])):
        if is_safe(arr,i,col):
            arr[i][col]=1
            NQueen(arr,i+1,ans+f"{i}-{col},")
            arr[i][col]=0

arr=[[0]*2 for i in range(2)]
NQueen(arr,0,"")
