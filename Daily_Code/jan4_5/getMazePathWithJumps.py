# def getMazePathWithJumps(sr,sc,dr,dc):
#     if sr==dr and sc==dc:
#         return [""]
#     temp=[]
#     for i in range(1,4):  #this loop will jump only upto 3. 
#         if sc<dc:
#             hpath=getMazePathWithJumps(sr,sc+i,dr,dc)
#             for j in hpath:
#                 temp.append(f'h{i}{j}')
#         if sc<dc and sr<dr:
#             dpath=getMazePathWithJumps(sr+i,sc+i,dr,dc)
#             for j in dpath:
#                 temp.append(f'd{i}{j}')
#         if sr<dr:
#             vpath=getMazePathWithJumps(sr+i,sc,dr,dc)
#             for j in vpath:
#                 temp.append(f'v{i}{j}')
#     return temp


#write getMazePathWithJumps Function with jumps upto wall of maze means if there are maze of size 5,5 then jumps will be upto 4
def getMazePathWithJumpsuptoWall(sr,sc,dr,dc):
    if sr==dr and sc==dc:
        return [""]
    temp=[]
    for i in range(1,dc+1):  #this loop will jump only upto 3. 
        if sc<dc:
            hpath=getMazePathWithJumpsuptoWall(sr,sc+i,dr,dc)
            for j in hpath:
                temp.append(f'h{i}{j}')

    for i in range(1,dc+1):
        if sc<dc and sr<dr:
            dpath=getMazePathWithJumpsuptoWall(sr+i,sc+i,dr,dc)
            for j in dpath:
                temp.append(f'd{i}{j}')
    
    for i in range(1,dr+1):
        if sr<dr:
            vpath=getMazePathWithJumpsuptoWall(sr+i,sc,dr,dc)
            for j in vpath:
                temp.append(f'v{i}{j}')
    return temp

print(getMazePathWithJumpsuptoWall(1,1,5,5))
# print(getMazePathWithJumpsuptoWall(1,1,4,4))
# print(getMazePathWithJumpsuptoWall(1,1,1,4))



