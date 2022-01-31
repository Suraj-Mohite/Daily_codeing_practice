#check whether input string contaons special character or not

def checkSpecialChar(myStr):
    for i in myStr:
        if not((ord(i)>=ord('a') and ord('i')<=ord('z'))or(ord(i)>=ord('A') and ord('i')<=ord('Z'))or(ord(i)>=ord('0') and ord(i)<=ord('9'))):
            return "String Contains Special Char"
    return "string doesnt contain special char"

print(checkSpecialChar("suraj1kldslihfisd]"))
