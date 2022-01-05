def printSubsequence(String,ans):
    if String=="":
        print(ans)
        return
    printSubsequence(String[1:],ans+String[0])
    printSubsequence(String[1:],ans)

printSubsequence('',"")