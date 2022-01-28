# Program to sort alphabetically the words form a string provided by the user

def sortWord(String):
    words=String.lower().split(' ')
    print(words)
    words.sort()
    print(" ".join(words))

sortWord("Program to sort alphabetically the words form a string provided by the user")