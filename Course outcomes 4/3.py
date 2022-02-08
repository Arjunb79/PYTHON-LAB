class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area_cal(self):
        self.area=self.__length*self.__width
        print("area=",self.area)
    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False

l1=int(input("enter the length of rectangle 1:"))
w1=int(input("enter the width rectangle 1:"))

l2=int(input("enter the length rectangle 2:"))
w2=int(input("enter the width rectangle 2:"))

ob1=Rectangle(l1,w1)
ob2=Rectangle(l2,w2)
ob1.area_cal()
ob2.area_cal()

if ob1 < ob2:
    print("second rectangle is large")
else:
    print("first rectangle is large or equal")


