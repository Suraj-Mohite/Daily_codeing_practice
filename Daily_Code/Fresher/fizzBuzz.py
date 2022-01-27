#if input is divisible by 3 return fizz if it is divisible fy 5 return Buzz if both then return fizzBuzz

def fizzBuzz(num):
    ans=""

    for n in range(1,num+1):
        if n%3==0 and n%5==0:
            print('FizzBuzz')
        elif n%3==0:
            print("Fizz")
        elif n%5==0:
            print("Buzz")
        else:
            print(n)

# fizzBuzz(50)

#by using Dictionary
def fizzBuzz1(num):
    Dict={3:"Fizz",5:"Buzz"}

    for n in range(1,num+1):
        ans=""
        for k,v in Dict.items():
            if n%k==0:
                ans+=v
        if not ans:
            ans=n
        print(ans)

fizzBuzz1(50)