#Display future leap years from current year to a final year entered by user.
a=int(input("enter the future year"))
b=int(input("enter the current year"))
while (b<=a):
    if b%100==0:
        if b%400==0:
            print(b)
    elif b%4==0:
        print(b)
    b+=1