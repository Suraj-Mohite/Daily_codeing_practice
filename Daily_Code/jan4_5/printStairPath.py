def printStairPath(num,ans):
    if num<0:
        return
    if num==0:
        print(ans)
        return
    for i in range(1,4):
        printStairPath(num-i,ans+str(i))

printStairPath(3,"")