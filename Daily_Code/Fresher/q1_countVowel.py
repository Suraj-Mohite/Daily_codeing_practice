#Program to count the number of each vowel in a string

def countVowels(String):
    map={}
    vowel=['a','e','i','o','u']
    for ch in String:
        ch=ch.lower()
        if ch in vowel:
            map[ch]=map.get(ch,0)+1 
    return map

print(countVowels("My nme Is surj Prksh Mohite"))

#using fromkeys()
# if any vowel is not present in the string then this function will keep is default value 0 as it is. means is any string is not contain any vowel then it will return dictionary with keys(vowel) and default value 0 whereas above function will return {}
def cntVowels(String):
    vowels='aeiou'
    ans=dict.fromkeys(vowels,0)
    for ch in String:
        if ch in ans:
            ans[ch]+=1
    return ans

print(cntVowels("My nme Is surj Prksh Mohite"))

