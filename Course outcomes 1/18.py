#Merge two dictionaries.

d1={"a":1,"b":2,"c":3,"d":4}
d2={"apple":1,"bat":2,"cat":3,"dog":4}
print(d1,"\n",d2)
d1.update(d2)
print(d1)