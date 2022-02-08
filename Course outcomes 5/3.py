import csv
ls=[]
f=open("dept.csv","r")
cr=csv.reader(f)
# fields=cr.next()
for l in cr:
    ls.append(l)
print(ls,"\n")