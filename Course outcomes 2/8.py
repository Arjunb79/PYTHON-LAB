#Accept a list of words and return length of longest word.
n=int(input("enter the limit"))
l=[]
m=[]
for x in range(0,n):
    w=input("enter the word")              #enter 4 words
    m.append(len(w))
    l.append(w)
print(l)
print(m)
print(" length longest word is=",max(m))