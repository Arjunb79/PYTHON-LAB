#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both

#a)Whether list are of same length
l1=[1,4,5,6,7,8,7]
l2=[4,5,6,7,8,9]
print(l1)
print(l2)
if len(l1)==len(l2):
    print("list have same length")
else:
    print("list is not in same length")

#b)whether list sums to same value

if sum(l1)==sum(l2):
    print("sums are same")
else:
    print("sums are not same")
print("sum of l1=",sum(l1))
print("sum of l2=",sum(l2))

#c)whether any value occur in both

l3=[x for x in l1 if x in l2]
if len(l3)<1:
    print("No value occure in both")
else:
    print("common values:",l3)