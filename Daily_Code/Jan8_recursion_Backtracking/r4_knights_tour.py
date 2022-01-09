def knights_tour(arr,row,col,move):
    if row<0 or col<0 or row>=len(arr) or col>=len(arr[0]) or arr[row][col]!=0:
        return
    if move==len(arr)*len(arr[0]):
        arr[row][col]=move
        for i in arr:
            print(i)
        arr[row][col]=0
        print()
        return
    arr[row][col]=move
    knights_tour(arr,row-2,col+1,move+1)
    knights_tour(arr,row-1,col+2,move+1)
    knights_tour(arr,row+1,col+2,move+1)
    knights_tour(arr,row+2,col+1,move+1)
    knights_tour(arr,row+2,col-1,move+1)
    knights_tour(arr,row+1,col-2,move+1)
    knights_tour(arr,row-1,col-2,move+1)
    knights_tour(arr,row-2,col-1,move+1)
    arr[row][col]=0

arr=[[0]*5 for i in range(5)]
# knights_tour(arr,2,3,1)
knights_tour(arr,2,0,1)