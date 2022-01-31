#Find the position from where the parenthesis is not balanced 
# Given a string str consisting of parenthesis from [ “(” , “)” , “{” , “}” , “[” , “]” ]. 
# If the String is perfectly balanced return 0 else return the index(starting from 1)at which the nesting is found to be wrong.

def imbalancedPara(myStr):
    stack=[]
    for i in range(len(myStr)):
        if len(stack)!=0:
            if myStr[i]==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return i+1
            elif myStr[i]=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return i+1
            elif myStr[i]=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return i+1
            else:
                stack.append(myStr[i])        
        else :
            if myStr[i]=="}" or myStr[i]==")" or myStr[i]=="]":
                return i+1
            else:
                stack.append(myStr[i])

    if len(stack)!=0:
            return len(myStr)+1
    return 0

print(imbalancedPara("{[()]}[]"))
print(imbalancedPara("[{]()}"))
print(imbalancedPara("}[{}]"))
print(imbalancedPara("{([]){"))
print(imbalancedPara("{{{{"))