def tripletSum(arr1,arr2,arr3,ans):
    n=len(ans)

    if n==3:
        print(ans)
        return 1

    if n==0:
        a=0
        for i in arr1:
            ans.append(i)
            a+=tripletSum(arr1,arr2,arr3,ans)
            ans.pop()
        return a
    
    if n==1:
        b=0
        for i in arr2:
            if i>=ans[0]:
                ans.append(i)
                b+=tripletSum(arr1,arr2,arr3,ans)
                ans.pop()
        return b

    if n==2:
        c=0
        for i in arr3:
            if i<=ans[1]:
                ans.append(i)
                c+=tripletSum(arr1,arr2,arr3,ans)
                ans.pop()
        return c

# print(tripletSum([3,5,7],[3,6],[4,6,9],[]))
print(tripletSum([1,3,5],[2,3],[1,2,3],[]))