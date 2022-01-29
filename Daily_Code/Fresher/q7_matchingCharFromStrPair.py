#Count the Number of matching characters in a pair of string
def countMatchingChar(myStr1,myStr2):
    d1={}.fromkeys(myStr1,0)
    for i in myStr2:
        if i in d1:
            d1[i]+=1
    cnt=0
    for i,j in d1.items():
        if j!=0:
            cnt+=1
    print(cnt)

# countMatchingChar("aabcddekll12@",'bb22ll@55k')
# countMatchingChar("abcdef",'defghia')


#using Find Function

def countMatchingChr(myStr1,myStr2):
    cnt=0
    j=0
    for i in myStr1:
        if myStr2.find(i)>=0 and j==myStr1.find(i):
            cnt+=1
        j+=1
    
    return cnt

# print(countMatchingChr("aabcddekll12@",''))

#using set Function

def countMatchingChr1(myStr1,myStr2):
    s1=set(myStr1)
    s2=set(myStr2)

    # res=s1.intersection(s2)
    res=s1 & s2
    return len(res)

# print(countMatchingChr1("aabcddekll12@",'bb2211@55k'))


#remove all duplicates from given string

#without order
# def removeDuplicate(myStr):
#     return "".join(set(myStr))

def removeDuplicate(myStr):
    ans=""
    for i in myStr:
        if i not in ans:
            ans+=i
    return ans

print(removeDuplicate("geeksforgeeks"))