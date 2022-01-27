#input: abaaaadddcbbacd output: a1b1a4d3c1b2a1c1d1
def compressStr(String):
    p1=0
    p2=0
    ans=""
    cnt=0
    n=len(String)
    while p1<n:
        if p2<n and String[p1]==String[p2]:
            cnt+=1
            p2+=1
        else:
            ans+=String[p1]+str(cnt)
            cnt=0
            p1=p2
    return ans

# print(compressStr("abaaaadddcbbacd"))


#input: abaaaadddcbbacd output: aba4d3c1b2acd
def compressStr1(String):
    p1=0
    p2=0
    ans=""
    cnt=0
    n=len(String)
    while p1<n:
        if p2<n and String[p1]==String[p2]:
            cnt+=1
            p2+=1
        else:
            if cnt==1:
                ans+=String[p1]
            else:
                ans+=String[p1]+str(cnt)
            cnt=0
            p1=p2
    return ans

# print(compressStr1("abaaaadddcbbacd"))


def compressStr2(String):
    n=len(String)
    if n==0:
        return "invalid input"
    letter=String[0]
    cnt=1
    ans=""
    for i in range(1,n+1):
        if i<n and String[i]==letter:
            cnt+=1
        else:
            ans+=letter+str(cnt)
            if i<n:
                letter=String[i]
            cnt=1
    return ans

# print(compressStr2("gfffffus"))

def compStr(String):
    n=len(String)
    if n==0:
        return "invalid input"
    ans=""
    cnt=1
    for i in range(n-1):
        if String[i]==String[i+1]:
            cnt+=1
        else:
            ans+=String[i]+str(cnt)
            cnt=1
    else:
        ans+=String[n-1]+str(cnt)
    return ans

print(compStr("afdghghgg"))
