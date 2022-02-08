from graphics1.circle import *
from graphics1.rectangle import *
from graphics1._3D_graphics.cuboid import *
from graphics1._3D_graphics.sphere import *



#CIRCLE
#area
print("Area of circle:")
r=int(input(" enter the radius:"))
result=cir_area(r)
print("area of circle is=",result,"\n")


#Perimeter
print("**Perimeter of Circle***")
result=cir_peri(r)
print("Perimeter of circle is=",result,"\n")


#RECTANGLE
#area
print("***Area of rectangle***")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
result=rec_area(l,b)
print("area of rectangle=",result,"\n")

#perimeter
print("***perimeter of rectangle***")
result=reac_peri(l,b)
print("perimeter=",result)

#cuboid
#area 
print("***area of cuboid***")
l=int(input("enter the length:"))
w=int(input("enter the width:"))
h=int(input("enter the height:"))
result=cub_area(l,w,h)
print("area=",result)

#perimeter
print("***perimeter of cuboid***")
result=cub_per(l,w,h)
print("primeter=",result)

#sphere
#area
print("***area of sphere***")
r=int(input("enter the radius:"))
result=sph_area(r)
print("area=",result)

#perimeter
print("***perimeter of sphere***")
result=sph_peri(r)
print("primeter=",result)

