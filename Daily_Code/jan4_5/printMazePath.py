#print all possible path to reatch from cell 1,1 to n,n
# def printMazePath(sr,sc,dr,dc,ans):
#     if sr==dr and sc==dc:
#         print(ans)
#         return
#     if sc<dc:
#         printMazePath(sr,sc+1,dr,dc,ans+"h")
#     if sr<dr:
#         printMazePath(sr+1,sc,dr,dc,ans+"v")


def printMazePath(sr,sc,dr,dc,ans):
    if sr>dr or sc>dc:
        return
    if sr==dr and sc==dc:
        print(ans)
        return
    
    printMazePath(sr,sc+1,dr,dc,ans+"h")
    printMazePath(sr+1,sc,dr,dc,ans+"v")

printMazePath(1,1,2,3,"")


def printMazePathDiagonal(sr,sc,dr,dc,ans):
    if sr==dr and sc==dc:
        print(ans)
        return
    if sc<dc:
        printMazePathDiagonal(sr,sc+1,dr,dc,ans+"h")
    if sc<dc and sr<dr:
        printMazePathDiagonal(sr+1,sc+1,dr,dc,ans+'d')
    if sr<dr:
        printMazePathDiagonal(sr+1,sc,dr,dc,ans+"v")

# printMazePathDiagonal(1,1,2,3,"")
