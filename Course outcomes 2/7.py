#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly

def string(s):
    if len(s)>=3:
        if s[-3:]=="ing":
            print(s+"ly")
        else:
            print(s+"ing")
        return s
    else:
        print(s+'ing')
s=input("enter the string \n")
string(s)
