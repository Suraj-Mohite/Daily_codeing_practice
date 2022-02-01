#Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

def cntAll(myStr):
    map={}
    for i in myStr:
        if i.isupper():
            map['Upper']=map.get('Upper',0)+1
        elif i.islower():
            map['Lower']=map.get('Lower',0)+1
        elif ord(i)>=ord('0') and ord(i)<=ord('9'):
            map['Numeric']=map.get('Numeric',0)+1
        else:
            map['Special']=map.get('Special',0)+1
    return map

print(cntAll('SurajMohit347JaN12'))