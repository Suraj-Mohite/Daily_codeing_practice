def permutationWithSpaces(Str,i,ans):
    if i==len(Str)-1:
        print(ans+Str[i])
        return
    permutationWithSpaces(Str,i+1,ans+Str[i]+" ")
    permutationWithSpaces(Str,i+1,ans+Str[i])

permutationWithSpaces("ACD",0,"")