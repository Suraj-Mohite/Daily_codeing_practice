code={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}

def printEncoding(num,ans):
    if len(num)==0:
        print(ans)
        return
    if num[0]=='0':
        return
    
    printEncoding(num[1:],ans+code[int(num[0])])
    if len(num)>=2 and int(num[:2])>26:
        return
    if len(num)>=2:
        printEncoding(num[2:],ans+code[int(num[:2])])

printEncoding('3',"")