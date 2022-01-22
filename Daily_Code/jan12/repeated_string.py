
def repeatedString(String,n,ans):
    if n==0:
        return ans
    if len(String)>=n:
        return ans+String[:n]

    r=n-len(String)
    return repeatedString(String,r,ans+String)
    
#abc

print(repeatedString("Suraj",47,""))