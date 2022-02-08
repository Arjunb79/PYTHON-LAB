#Create a single string separated with space from two strings by swapping the
#character at position 1.


s1=input("enter the string1")
s2=input("enter the string2")

print(s2[0]+s1[1:]+" "+s1[0]+s2[1:])