def getStairPath(num):
    if num==0:
        return [""]
    if num<0:
        return []
    temp=[]
    arr1=getStairPath(num-1)
    if arr1:
        for i in arr1:
            temp.append('1'+i)
    arr2=getStairPath(num-2)
    if arr2:
        for i in arr2:
            temp.append('2'+i)
    arr3=getStairPath(num-3)
    if arr3:
        for i in arr3:
            temp.append('3'+i)
    return temp

print(getStairPath(4))
print(getStairPath(2))
print(getStairPath(0))