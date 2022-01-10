def GenerateBalancedParentheses(n):
    result=[]
    def inner(open,close,ans):
        if open==0 and close==0:
            result.append(ans)
            return
        if open>0:
            inner(open-1,close,ans+"(")
        if open!=close:
            inner(open,close-1,ans+")")

    inner(n,n,"")
    return result

print(GenerateBalancedParentheses(3))