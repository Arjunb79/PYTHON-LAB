f1=open("text.txt","r")
f2=open("text1.txt","w+")
fr=f1.readlines()
for i in range(0,len(fr)):
    if(i%2!=0):
        f2.write(fr[i])
    else:
        pass
#f2r=open("text1.txt","r")
fr2=f2.read()
print(fr2)