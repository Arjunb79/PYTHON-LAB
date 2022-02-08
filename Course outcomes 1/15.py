#Print out all colors from color-list1 not contained in color-list2.

cl1=['red','green','yellow','violet','blue']
cl2=['red','purple','white','yellow','gray']
print("Print out all colors from color-list1 not contained in color-list2.")
print([x for x in cl1 if x not in cl2])