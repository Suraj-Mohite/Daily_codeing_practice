#print all permutations with case change if string contains any numeric value then keep it as it is

def permWithLetterCase(Str,i,ans):
    if i==len(Str):
        print(ans)
        return
    if Str[i].isupper():
        permWithLetterCase(Str,i+1,ans+Str[i].lower())
    elif Str[i].islower():
        permWithLetterCase(Str,i+1,ans+Str[i].upper())
    
    permWithLetterCase(Str,i+1,ans+Str[i])

permWithLetterCase("5p22",0,"")
    