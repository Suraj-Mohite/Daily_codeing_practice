key={'1':'abc','2':'def','3':'ghi','4':'jkl','5':'mnop','6':'qrst','7':'uv'}

def printKeypadComb(num,ans):
    if num=="":
        print(ans)
        return
    
    for i in key[num[0]]:
        printKeypadComb(num[1:],ans+i)

printKeypadComb('123',"")
printKeypadComb('',"")