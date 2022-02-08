#Store a list of first names. Count the occurrences of ‘a’ within the list

w=['arjun','alan','arun','thomas','afeef']
n=0
for x in w:
    n=n+x.count("a")
print(n)