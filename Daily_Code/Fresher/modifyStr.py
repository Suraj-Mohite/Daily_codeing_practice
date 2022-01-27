def modifyString(String):
    ans=""

    for i in String:
        if i.isupper():
            ans+=i.lower()
        elif i.islower():
            ans+=i.upper()
        elif i=='_':
            ans+="."
        else:
            ans+=i
    return ans

print(modifyString("Sur@j_Is_mY_Name"))