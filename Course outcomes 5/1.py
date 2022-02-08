fr=open("text2.txt","r")
l=fr.readlines()
for line in l:
    print(line)
fr.close()


# with open("text2.txt","r")as f:
#     r=f.readlines()
#     for l in r:
#         print(l)
