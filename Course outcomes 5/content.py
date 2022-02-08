with open("hi.txt","r") as f1,open("t.txt","w") as f2:
    for line in f1:
        f2.write(line)
        print(line)