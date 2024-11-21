#Write a python program  to calculate the  area if circle using radius formula
from xml.sax.saxutils import prepare_input_source

# area =pie r^2

#step1 : figure out inputs and  out prepare_input_source()
"""input -> r-> data type ._ float
Pi=3.14
Power-> pow or **-> any 
output->float-area, print area
#step 2:
# rough logic =area =3.14*pow(r,2)"""

# step 3:
radius = float (input("Enter  the radius of the  circle:\n"))
print(radius)
area =3.14*(radius**2)
print ("Area of the circle is -> ", area)
print (f"Area of the circle is -> : {area:.3f}")


"""Single line code for above req"""
#print(3.14*(float(input("Enter the radius of the circle\n"))**2))
