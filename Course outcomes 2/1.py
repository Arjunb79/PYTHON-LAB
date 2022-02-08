#Program to find the factorial of a number

n=int(input("enter the number"))
f=1
for x in range(1,n+1):
    f=f*x
print("factorial=",f)