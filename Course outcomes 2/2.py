#Generate Fibonacci series of N terms
n=int(input("enter te number"))
a=0
b=1
sum=0
i=1
print("fibonacci series:")
while(i<=n):
    print(sum)
    i+=1
    a=b
    b=sum
    sum=a+b
