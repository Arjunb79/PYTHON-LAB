#Accept an integer n and compute n+nn+nnn.

n=int(input("enter the number n="))
a=str(n)
b=a+a
c=a+a+a
print(a,"+",b,"+",c)
b=int(b)
c=int(c)
s=n+b+c
print(s)