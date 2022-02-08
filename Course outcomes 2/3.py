#Find the sum of all items in a list

l=[1,2,3,4,6,7,8,9]
print("sum of list=",sum(l))

li=input("enter the numbers separated with commas=")
li1=li.split(",")

#method1
s=0
print("list elements are...")
print(li1)

for x in li1:
    s=s+int(x)
print("sum of all items in a list=",s)