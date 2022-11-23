

from cmath import pi


# SCRIPT FOR SQUARE AREA
square_side = float(input("What is the length of a side of a square? "))
area1 = square_side ** 2

print(f"The area of a square is: {area1}")

#########################################
#SCRIPT FOR RECTANGLE AREA
rectangle_length = float(input("What is the length of a rectangle? " ))
rectangle_width = float(input("What is the width of the rectangle? "))
area2 = rectangle_length * rectangle_width

print(area2)

#########################################
#AREA OF A CIRCLE
radius = float(input("What is the radius of a circle? "))
area3 = pi * (radius ** 2)

print(f"The area of a circle is: {area3:.3f}")
