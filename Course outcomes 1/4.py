#Count the occurrences of each word in a line of text.
s1=input("enter the word")
for i in list(set(s1.split())):
    print(i,"has occured ",s1.split().count(i),"times")
