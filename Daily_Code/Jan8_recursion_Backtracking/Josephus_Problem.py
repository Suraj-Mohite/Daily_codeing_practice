def JosephusProblem(n,k):
    if n==0:
        return "invalid input"
    arr=list(range(1,n+1))
    k=k-1  #if steps =3 then we have to start counting from starting index
    def JosephusProblemInner(arr,ind,k):
        if len(arr)==1:
            return arr[0]
        
        ind=(ind+k)%len(arr) # if steps goes out of the array then it will again start from 0 index
        arr.remove(arr[ind])
        return JosephusProblemInner(arr,ind,k)

    return JosephusProblemInner(arr,0,k)

print(JosephusProblem(0,7))