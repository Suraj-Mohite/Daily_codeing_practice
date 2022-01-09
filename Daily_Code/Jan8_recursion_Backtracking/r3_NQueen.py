def is_safe(arr,i,j):
    row=i
    while(row>=0):
        if arr[row][j]==1:
            return False
        row-=1
    row=i
    col=j
    while(row>=0 and col>=0):
        if arr[row][col]==1:
            return False
        row-=1
        col-=1

    row=i
    col=j
    while(row>=0 and col<len(arr)):
        if arr[row][col]==1:
            return False
        row-=1
        col+=1

    return True
    


def NQueen(arr,i,ans):
    if i==len(arr):
        print(ans+".")
        return
    for col in range(len(arr)):
        if is_safe(arr,i,col)==True:
            arr[i][col]=1
            NQueen(arr,i+1,ans+f"{i}-{col},")
            arr[i][col]=0

arr=[[0]*5 for i in range(5)]
NQueen(arr,0,"")
