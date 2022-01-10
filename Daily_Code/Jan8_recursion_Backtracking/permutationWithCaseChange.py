def permutationWithCaseChange(Str,i,ans):
    if i==len(Str):
        print(ans)
        return
    permutationWithCaseChange(Str,i+1,ans+Str[i])     
    permutationWithCaseChange(Str,i+1,ans+Str[i].upper())        

permutationWithCaseChange('ab',0,"")   