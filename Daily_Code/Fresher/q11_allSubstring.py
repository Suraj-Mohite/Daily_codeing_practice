#Write a program to get all substrings of given string

def allSubString(myStr):
    for i in range(len(myStr),-1,-1):
        for j in range(i):
            print(myStr[j:i])

allSubString("Geeky")