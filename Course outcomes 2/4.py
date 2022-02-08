n=int(input("enter the upper limit"))
m=int(input("enter lower limit"))
l1=[]
l2=[]
for x in range(1,n+1):
    if x%2==0:
        l1.append(x)
for y in l1:
    for z in range(1,y):
        if z*z ==y:
            l2.append(y)
print(l2)