# Program to transpose a matrix using nested loop



def transposeMatrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    ans=[[0]*row for i in range(col)]

    for i in range(row):
        for j in range(col):
            ans[j][i]=matrix[i][j]
    print(ans)

# transposeMatrix([[1,2,3],[4,5,6],[7,8,9]])
# transposeMatrix([[1,2,3],[4,5,6]])

def transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    ans=[[matrix[j][i] for j in range(row)]for i in range(col)]
    print(ans)

transpose([[1,2,3],[4,5,6],[7,8,9]])

# Program to transpose a matrix using nested loop
#if the input is Square MAtrix then we can solve same question with O(1) space complexity for non square matrix it will give error

def transposeSquareMatrix(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if i<=j:
                Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]

# Matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(Matrix)
# transposeSquareMatrix(Matrix)
# print(Matrix)
