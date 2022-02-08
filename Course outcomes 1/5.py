#5. Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.

l1=[]
l1=[int(item) for item in input("enter the values").split()]
print("input=",l1)
x=["over" if x > 100 else x for x in l1]
l1=list(x)
print(l1)