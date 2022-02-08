fr=open("text2.txt","r")
fw=open("text2.txt","a")
for line in fr:
    fr.write(line.capitalize())
    print(line)
fr.close()