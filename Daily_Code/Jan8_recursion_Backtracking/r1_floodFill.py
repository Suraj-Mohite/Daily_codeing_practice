def floodFill(arr,i,j,ans):

    if i<0 or j<0 or i==len(arr) or j==len(arr[0]) or arr[i][j]==1 :
        return

    if i==len(arr)-1 and j==len(arr[0])-1:
        print(ans)
        return
    arr[i][j]=1
    floodFill(arr,i-1,j,ans+'T ')
    floodFill(arr,i,j-1,ans+'L ')
    floodFill(arr,i+1,j,ans+'D ')
    floodFill(arr,i,j+1,ans+'R ')
    arr[i][j]=0

floodFill([[0,1,0,0,0,0,0],
           [0,1,0,1,1,1,0],
           [0,0,0,0,0,0,0],
           [1,0,1,1,0,1,1],
           [1,0,1,1,0,1,1],
           [1,0,0,0,0,0,0]
           ],0,0,"")