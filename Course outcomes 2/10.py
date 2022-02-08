#Generate all factors of a number.

n=int(input("enter the number"))
print("factors=")
for x in range(1,n+1):
    if n%x==0:
        print(x," ",end="")