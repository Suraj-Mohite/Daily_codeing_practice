def uniqueSub(Str,i,ans,map={}):
    if i==len(Str):
        map[ans]=map.get(ans,0)+1
        if map[ans]==1:
            print(ans)
        return
    uniqueSub(Str,i+1,ans+Str[i],map)
    uniqueSub(Str,i+1,ans,map)

uniqueSub("aab",0,"")