#Get a string from an input string where all occurrences of first character replaced with
#‘$’, except first character.
s=input("enter the string \n")
a=s[0]
b=s[1:]
c=b.replace(a,"$")
sum=a+c
print(sum)