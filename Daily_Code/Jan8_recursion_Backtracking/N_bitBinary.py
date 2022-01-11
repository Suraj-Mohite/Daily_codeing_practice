"""
Given a positive integer N, the task is to find all the N bit binary numbers having more than or equal 1’s than 0’s for any prefix of the number.

Example 1:

Input:  N = 2
Output: 11 10
Explanation: 11 and 10 have more than 
or equal 1's than 0's
Example 2:

Input:  N = 3
Output: 111 110 101
Explanation: 111, 110 and 101 have more 
than or equal 1's than 0's
User Task:
Your task is to complete the function NBitBinaryinner() which takes a single number as input and returns the list of strings in decreasing order. You need not take any input or print anything.

Expected Time Complexity: O(|2N|)
Expected Auxiliary Space: O(2N)

Constraints:
1 <= N <= 20
"""
# here number of 1s should be always >= number of 0s in every prefix of n
# logic: if no of 1 is greater than no of 0 then there is use to call function which will add 0 coz we already have one so it always will be greater than zero

def NbitBinary(n):
    def NBitBinaryinner(n,ans,one,zero):
        if n==0:
            print(ans)
            return
        NBitBinaryinner(n-1,ans+'1',one+1,zero)
        if one>zero:        #it means 1s >= 0s no of 1s can be > or equal to no of 0s in any prefix
            NBitBinaryinner(n-1,ans+'0',one,zero+1)

    NBitBinaryinner(n,"",0,0)

# NbitBinary(4)


# here number of 1s should be always > number of 0s in every prefix of n
def NbitBinary1gt0(n,ans,one=0,zero=0):
    if n==0:
        print(ans)
        return
    NbitBinary1gt0(n-1,ans+'1',one+1,zero)
    if one>zero+1: #it means 1s > 0s no of 1s can not be equal to no of 0s in any prefix
        NbitBinary1gt0(n-1,ans+'0',one,zero+1)
# NbitBinary1gt0(3,"")


# here number of 1s should be always >= number of 0s in every POSTFIX of n
def NBitBinaryPostfix(n,ans,one,zero):
    if n==0:
        print(ans)
        return
    NBitBinaryPostfix(n-1,'1'+ans,one+1,zero)
    if one>zero:
        NBitBinaryPostfix(n-1,'0'+ans,one,zero+1)

# NBitBinaryPostfix(3,"",0,0)


# here number of 1s should be always >= number of 0s in every POSTFIX of n
def NBitBinaryPostfix1gt0(n,ans,one,zero):
    if n==0:
        print(ans)
        return
    NBitBinaryPostfix1gt0(n-1,'1'+ans,one+1,zero)
    if one>zero+1:
        NBitBinaryPostfix1gt0(n-1,'0'+ans,one,zero+1)

NBitBinaryPostfix1gt0(3,"",0,0)

