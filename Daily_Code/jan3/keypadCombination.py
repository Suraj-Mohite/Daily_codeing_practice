key={'1':'abc','2':'def','3':'ghi','4':'jkl','5':'mnop','6':'qrst','7':'uv'}

def keypadComb(num):
    if num=="":
        return [""]
    arr=keypadComb(num[1:])
    temp=[]
    for i in key[num[0]]:
        for j in arr:
            temp.append(i+j)
    return temp

print(keypadComb('125'))
print(keypadComb(''))
