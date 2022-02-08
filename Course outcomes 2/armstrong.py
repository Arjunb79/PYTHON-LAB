def arm(n):    
    sum=0
    temp=n
    while temp>0:
        d=temp%10
        sum+=d**3
        temp//=10
    if sum==n:
        print(n," is amtrong")
    else:
        print(n," not amtrong") 
             
n=int(input("enter the number to check armstrong or not"))
arm(n)