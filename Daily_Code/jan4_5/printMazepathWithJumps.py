def printMazePathWithJumps(sr,sc,dr,dc,ans=""):
    if sr>dr or sc>dc:
        return   
    if sr==dr and sc==dc:
        print(ans)
        return

    #horizontal
    for i in range(1,dc+1):
        printMazePathWithJumps(sr,sc+i,dr,dc,f'{ans}h{i}')

    #diagonal
    for i in range(1,dc+1):
        printMazePathWithJumps(sr+i,sc+i,dr,dc,f'{ans}d{i}')

    #vertical
    for i in range(1,dr+1):
        printMazePathWithJumps(sr+i,sc,dr,dc,f'{ans}v{i}')


printMazePathWithJumps(1,1,4,2,"")