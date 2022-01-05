#print all permutations of the string

def printPermutation(String,ans=""):  #default value of ans is ""
    if len(String)==0:
        print(ans)
        return
    for i in range(len(String)):
        printPermutation(String[:i]+String[i+1:],ans+String[i])

# printPermutation('abc',"")

#print all palindromic permutations of the string

def palindromicPermutations(String,ans=""):
    if len(String)==0:
        if ans==ans[::-1]:
            print(ans)
        return

    for i in range(len(String)):
        palindromicPermutations(String[:i]+String[i+1:],ans+String[i])

palindromicPermutations('aba')