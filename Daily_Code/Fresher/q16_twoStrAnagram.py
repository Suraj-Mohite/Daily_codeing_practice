#Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.

def createDict(myStr):
    map={}
    for i in myStr:
        map[i]=map.get(i,0)+1
    return map

# def anagram(str1,str2):
#     dict1=createDict(str1)
#     dict2=createDict(str2)

#     cnt=0
#     print(dict1)
#     print(dict2)
#     for key in dict1:
#         if key in dict2:
#             if dict1[key] > dict2[key]:
#                 n=dict1[key]-dict2[key]
#                 cnt+=n
#                 dict1[key]-=n

#             elif dict1[key] < dict2[key]:
#                 n=dict2[key]-dict1[key]
#                 cnt+=n
#                 dict2[key]-=n
            
#         else:
#             cnt+=dict1[key]
#             del dict1[key]
#     print(dict1)
#     print(dict2)

# anagram('bcadeh','hea')