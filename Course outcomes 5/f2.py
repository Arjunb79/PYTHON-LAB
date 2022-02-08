s="hai all"
fw=open("t.txt","w")
fw.write(s)
fw.close()
fr=open("t.txt","r")
print(fr.read())
fr.close()