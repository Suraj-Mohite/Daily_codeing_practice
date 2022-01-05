# sr-source row
# sc-source column
# dr-destination row
# dc-destination column

#one way to write code 
def getMazePath(sr,sc,dr,dc):
    if sr>dr or sc>dc:
        return []
    if sr==dr and sc==dc:
        return [""]
    
    arr=getMazePath(sr+1,sc,dr,dc)
    temp=[]
    for i in arr:
        temp.append('v'+i)
    
    arr=getMazePath(sr,sc+1,dr,dc)
    for i in arr:
        temp.append('h'+i)
    return temp

# print(getMazePath(1,1,3,3))
# print(getMazePath(1,1,2,2))
# print(getMazePath(1,1,2,3))
# print(getMazePath(1,1,1,1))


#second way to write code

def getMazePath1(sr,sc,dr,dc):
    if sr==dr and sc==dc:
        return [""]
    temp=[]
    if sr<dr:
        vpath=getMazePath1(sr+1,sc,dr,dc)
        for i in vpath:
            temp.append('v'+i)
    if sc<dc:
        hpath=getMazePath1(sr,sc+1,dr,dc)
        for i in hpath:
            temp.append('h'+i)
    return temp

# print(getMazePath1(1,1,3,3))
# print(getMazePath1(1,1,2,2))
# print(getMazePath1(1,1,2,3))
# print(getMazePath1(1,1,1,1))

# Q2 get maze path by considering row column and diagonal way

def getMazePathDiagonal(sr,sc,dr,dc):
    if sr==dr and sc==dc:
        return [""]
    temp=[]

    if sr<dr:
        vpath=getMazePathDiagonal(sr+1,sc,dr,dc)
        for i in vpath:
            temp.append('v'+i)

    if sr<dr and sc<dc:
        dpath=getMazePathDiagonal(sr+1,sc+1,dr,dc)
        for i in dpath:
            temp.append('d'+i)
    if sc<dc:
        hpath=getMazePathDiagonal(sr,sc+1,dr,dc)
        for i in hpath:
            temp.append('h'+i)
    return temp

print(getMazePathDiagonal(1,1,3,3))
# print(getMazePathDiagonal(1,1,1,3))
# print(getMazePathDiagonal(1,1,2,2))
# print(getMazePathDiagonal(1,1,1,1))
# print(getMazePathDiagonal(1,1,0,0))