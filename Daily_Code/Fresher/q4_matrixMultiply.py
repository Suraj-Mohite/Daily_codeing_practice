
def matrixMultiply(arr1,arr2):
    n=len(arr1)
    m=len(arr1[0])
    n1=len(arr2)
    m1=len(arr2[0])

    if m==n1:
        ans=[[0]*m1 for i in range(n)]
    else:
        return "Invalid Input"
    for i in range(n):
        for j in range(m):
            for k in range(m):
                ans[i][j]+=arr1[i][k]*arr2[k][i]
    print(ans)

matrixMultiply([[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]],
    
    [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]])