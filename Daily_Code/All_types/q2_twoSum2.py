# def twoSum2(arr,target):
#     p1=0
#     p2=len(arr)-1
#     ans=[]
#     while p1<p2:
#         if arr[p1]+arr[p2]>target:
#             p2-=1
#         elif arr[p1]+arr[p2]<target:
#             p1+=1
#         else:
#             ans.append([arr[p1],arr[p2]])
#             p1+=1
#     return ans

# print(twoSum2([2, 3, 4, 5, 6, 7, 8, 9,10],16))


# x={10,20,30,40,50}
# y={1,5,20,30,4,6}
# w=y.difference(x)
# print(w)
# print(y-x)

# d='suraj'
# print(d,d[::-1])

# def deco(func):
#     def inner(s):
#         ss=s.upper()
#         return func(ss)
#     return inner

# @deco
# def actual(s):
#     return s

# print(actual("suraj"))

# a={1,2,3,5}
# b={1,2,3,6}
# c={1,2,3,6}
# for (x,y,z) in zip(a,b,c):
#     print(x,y,z)
# print()

# x=lambda a,b:a+b
# print(x(6,2))

import copy

# l1=[10,20,30,[40,50],60]
# l2=l1
# l1[0]=67
# print(l1)
# print(l2)  #aliasing

# l1=[10,20,30,[40,50],60]
# l2=l1.copy()
# l1[0]=67
# print(l1)
# print(l2) copy

# l1=[10,20,30,[40,50],60]
# l2=l1.copy()
# l1[3][0]=67
# print(l1)
# print(l2) #disadvantage of copy

# l1=[10,20,30,[40,50],60]
# l2=copy.copy(l1)
# l1[3][0]=67
# print(l1)
# print(l2) #disadvantage of copy

# l1=[10,20,30,[40,50],60]
# l2=copy.deepcopy(l1)
# l1[3][0]=67
# print(l1)
# print(l2) #deep copy

# def fib(n):
#     p,q=0,1
#     while(p< n):
#         yield p
#         p,q=q,p+q

# x=fib(10)
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())

# for i in fib(10):
#     print(i)


# s="suraj is my name"
# a=s.split(' ')
# print(a)
# print(" ".join(a))

# def fun(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(type(args))
#     print(type(kwargs))
#     print(kwargs)

# fun(1,2,5,6,9,6,3,num1=55,n2=69)

# import random

# print(random.randrange(1,20,2))

# a='asdf45@62'
# print(a.isalnum())

# def main():
#     print('sss')

# if __name__=='__main__':
#     main()

class test:
    def fun(self):
        print("inside fun")

def gun():
    print("sss")

obj=test()
obj.fun=gun
obj.fun()