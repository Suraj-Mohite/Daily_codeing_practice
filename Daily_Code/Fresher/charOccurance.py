#find least occurance of character in string

def leastOccurance(String):
    Dict={}
    n=len(String)
    for i in String:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    # min=n
    ans=""
    # for k,v in Dict.items():
    #     if v<min:
    #         min=v
    #         ans=k

    ans=min(Dict,key=Dict.get)
    return ans

# print(leastOccurance("paaaassdddffccoo"))

def cntOccur(String,ch):
    Dict={}
    for i in String:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    
    if ch in Dict:
        return Dict[ch]
    return 0

print(cntOccur("hgjhgjhhghgggggggghggggaaa",'p'))
