#write a program to print Even length word in string

def evenLengthWord(myStr):
    arr=myStr.split(' ')

    for i in arr:
        if len(i)%2==0:
            print(i)

evenLengthWord("My name is suraj prakash mohite")