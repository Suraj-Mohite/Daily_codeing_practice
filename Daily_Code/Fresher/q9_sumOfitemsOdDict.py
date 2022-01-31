#Python program to find the sum of all items in a dictionary

#approach1
# def chkSumOfItemsOfDict(map):
#     return sum(map.values()) #it will give exception for second test case

def chkSumOfItemsOfDict(map):
    sum=0
    for key,val in map.items():
        if type(val)==int or type(val)==float:
            sum+=val
    return sum
print(chkSumOfItemsOfDict({'a': 100.32, 'b':200, 'c':300}))
print(chkSumOfItemsOfDict({'a': '100', 'b':'200', 'c':'300'}))
print(chkSumOfItemsOfDict({'x': 25, 'y':18, 'z':45}))