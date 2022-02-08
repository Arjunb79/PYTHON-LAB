#a)Generate positive list of numbers from a given list of integers
x=[-1,2,-4,6,10,15,17,22,34,37,100]
a=[x for x in x if x>0]
print(a)

#b)Square of N numbers
n=int(input("enter the limit"))
r=[x*x for x in range(n+1)]
print(r)

#c)Form a list of vowels selected from a given word

s=(input("enter the string"))
l=['a','e','i','o','u','A','E','I','O','U']
n=[x for x in s if x in l]
print(n)

#d)List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

n=input("enter the word")
a=[ord(x) for x in n]
print(a)

